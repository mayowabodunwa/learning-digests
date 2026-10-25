#!/usr/bin/env bash
# Commit and push ONE finished digest, so a long backfill never loses work it
# has already done. Called by the producing agent after each unit.
#
#   publish_digest.sh <slug>
#
# Only ever stages that digest and its sidecar entry. It deliberately does not
# touch digests.json, index.html or TRACKER.md: several producer jobs run at
# once, and those three are the only files they would collide on. A later step
# merges the sidecars and rebuilds the index once.
set -euo pipefail

slug="${1:?usage: publish_digest.sh <slug>}"
html="docs/digests/${slug}.html"
entry="docs/_entries/${slug}.json"

[ -f "$html" ]  || { echo "::error::$html does not exist"; exit 1; }
[ -f "$entry" ] || { echo "::error::$entry does not exist (write the sidecar first)"; exit 1; }

git config user.name  "content-bot"
git config user.email "content-bot@users.noreply.github.com"
git add "$html" "$entry"
git commit -q -m "Digest: ${slug}" || { echo "nothing to commit for ${slug}"; exit 0; }

for attempt in 1 2 3 4 5 6 7 8; do
  git pull --rebase --autostash -q origin main || true
  if git push -q origin main 2>/dev/null; then
    echo "published ${slug} (attempt ${attempt})"
    exit 0
  fi
  echo "push for ${slug} rejected on attempt ${attempt}; retrying"
  sleep $((attempt * 3))
done

echo "::error::could not push ${slug} after 8 attempts"
exit 1
