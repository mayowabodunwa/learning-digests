#!/usr/bin/env python3
"""Merge per-digest sidecar entries into docs/digests.json.

The backfill runs several producer jobs in parallel. If each appended to
docs/digests.json directly they would conflict on every push, so each instead
drops one sidecar file at docs/_entries/<slug>.json. This merges them in,
deduping by slug (existing entries win, so a re-run is idempotent) and leaving
docs/digests.json in the same shape build_index.py already expects.
"""
import argparse, glob, json, os, sys

FIELDS = ("slug", "book", "ch", "title", "date")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--keep-sidecars", action="store_true",
                    help="don't delete the sidecars after merging")
    a = ap.parse_args()

    manifest = os.path.join(a.docs, "digests.json")
    items = json.load(open(manifest)) if os.path.exists(manifest) else []
    seen = {d["slug"] for d in items}

    added, skipped, bad = 0, 0, []
    for p in sorted(glob.glob(os.path.join(a.docs, "_entries", "*.json"))):
        try:
            e = json.load(open(p))
        except json.JSONDecodeError as exc:
            bad.append(f"{os.path.basename(p)}: {exc}")
            continue
        missing = [f for f in FIELDS if not e.get(f)]
        if missing:
            bad.append(f"{os.path.basename(p)}: missing {', '.join(missing)}")
            continue
        if not os.path.exists(os.path.join(a.docs, "digests", e["slug"] + ".html")):
            bad.append(f"{os.path.basename(p)}: no digest html for slug {e['slug']}")
            continue
        if e["slug"] in seen:
            skipped += 1
        else:
            items.append({f: e[f] for f in FIELDS})
            seen.add(e["slug"])
            added += 1
        if not a.keep_sidecars:
            os.remove(p)

    json.dump(items, open(manifest, "w"), indent=2)
    print(f"merge-entries: +{added} new, {skipped} already present, {len(items)} total")
    for b in bad:
        print(f"::warning::merge-entries skipped {b}")
    # Sidecars that failed validation are a content problem, not a reason to lose
    # the rest of the batch, so this still exits 0.
    return 0


if __name__ == "__main__":
    sys.exit(main())
