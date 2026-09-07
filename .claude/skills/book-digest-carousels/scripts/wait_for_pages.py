#!/usr/bin/env python3
"""Block until GitHub Pages actually serves this batch's digests.

The workflow commits `docs/` and then Pages rebuilds **asynchronously**. If the link
email goes out before that rebuild finishes, every "Read the digest" button 404s for a
minute or three, which is exactly what a reader hits when they open the email straight
away. Publishing first is only half the fix: this waits for the content to really be
live before the email is sent.

Polls the newest batch's first digest URL until it returns 200, then exits 0. If it
never comes up within the timeout it still exits 0 with a warning, so a slow Pages build
delays the email rather than losing the batch.

Usage:
    python wait_for_pages.py --docs docs --site-base-url "$SITE_BASE_URL"
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request


def batch_urls(docs, base):
    """URLs for the most recent date in the manifest (the batch just produced)."""
    manifest = os.path.join(docs, "digests.json")
    if not os.path.exists(manifest):
        return []
    items = json.load(open(manifest, encoding="utf-8"))
    if not items:
        return []
    latest = max(d.get("date", "") for d in items)
    base = (base or "").rstrip("/")
    if not base:
        return []
    return [f"{base}/digests/{d['slug']}.html"
            for d in items if d.get("date", "") == latest]


def status(url, timeout=10):
    req = urllib.request.Request(url, method="HEAD",
                                 headers={"User-Agent": "learning-digests-wait"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--site-base-url", default=os.environ.get("SITE_BASE_URL", ""))
    ap.add_argument("--timeout", type=int, default=600, help="seconds to wait (default 600)")
    ap.add_argument("--interval", type=int, default=15)
    args = ap.parse_args()

    urls = batch_urls(args.docs, args.site_base_url)
    if not urls:
        print("wait-for-pages: no batch URLs to check (no manifest entries or no base URL)")
        return 0

    # One URL is enough: Pages publishes the whole commit at once.
    url = urls[0]
    print(f"wait-for-pages: waiting for {url}")
    deadline = time.time() + args.timeout
    attempt = 0
    while time.time() < deadline:
        attempt += 1
        code = status(url)
        if code == 200:
            print(f"wait-for-pages: live after {attempt} check(s); "
                  f"emailing {len(urls)} link(s)")
            return 0
        print(f"  check {attempt}: HTTP {code or 'no response'}, retrying in {args.interval}s")
        time.sleep(args.interval)

    msg = (f"Pages did not serve {url} within {args.timeout}s; "
           f"sending the email anyway, links may 404 briefly")
    print(f"wait-for-pages: {msg}")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::warning::{msg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
