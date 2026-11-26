# Pull Request: Add Review Finding Triage

## Summary
Adds a small Python utility for collecting AI and human code review findings, recording justified reviewer decisions, prioritizing unresolved findings, and exporting a Markdown review log.

## Changes
- Added `review_triage.py` with validated findings, severity ordering, accept/reject/defer decisions, rationale tracking, and Markdown output.
- Added `test_review_triage.py` with coverage for validation, ordering, decisions, escaping, and empty reports.
- Added this PR description.

## Context
This feature supports the AI code review simulator workflow by making it easier to compare AI and human feedback and document why a suggestion was accepted, rejected, or deferred. No related issue is linked; the motivation is the project task.

## Verification
`python -m unittest discover -s ai_code_review_simulator -v` — 7 tests passed.
