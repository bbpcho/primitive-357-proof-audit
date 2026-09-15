# Independent public removal verification

Checked 2026-09-15T12:56:48.545985+00:00. All nine assertions in `PUBLIC_REMOVAL_VERIFICATION.json` passed.

The public API no longer lists companion asset **565450862** or verified-ZIP asset **563394734**. Their individual asset API endpoints and their original download URLs return **HTTP 404**; redirects were followed and separate cache-busted URL checks also returned 404.

The unaffected p=5 asset **561595084** and rank asset **561674379** remain listed with their original SHA-256 digests. Public Git main remains **8e1b03f6084339ab9286b4e6c8c1618abbfb75c7**. The before/after API records and the exact response details are preserved alongside this report.

This verifies withdrawal of the identified accessible public GitHub downloads. It does not imply deletion of previous external downloads or caches outside the checked responses. See `PUBLIC_COPY_INVENTORY.md` for containment evidence and the full-history check.
