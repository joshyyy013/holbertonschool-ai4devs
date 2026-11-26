# AI Review Log

**Tool:** ChatGPT  
**Feature:** Add review finding triage  
**Review scope:** `review_triage.py` and `test_review_triage.py` on `main`  
**Review status:** Reviewed in ChatGPT. No review was posted to a GitHub PR.

## Review Prompts

- **Security:** Review how the utility validates inputs and renders review text. Flag cases where input can change the structure of the Markdown report.
- **Performance:** Trace the filtering, sorting, and rendering paths. Identify unnecessary work and explain when it would matter.
- **Maintainability:** Check whether the public API enforces its documented rules and whether the tests cover the behaviors callers rely on.

## Inline Comments

1. **Security — `review_triage.py:119–127`**  
   The report title goes directly into a Markdown heading. A title containing a line break can spill into the body and change the report layout. Require a single-line title or normalize line breaks before rendering.

2. **Security — `review_triage.py:136`**  
   The cell formatter replaces `\n` but leaves standalone `\r` characters and only partly handles Windows-style line endings. Normalize line breaks with `splitlines()` before escaping table separators.

3. **Maintainability — `review_triage.py:58`**  
   The line number check enforces a lower bound but accepts values such as `1.5` and `True`. Validate that the value is a positive integer and explicitly exclude booleans.

4. **Maintainability — `review_triage.py:64`**  
   A `Finding` can be created with a blank or invalid value for `severity` or `source` despite the enum annotations. This can fail later during sorting or rendering. Validate the enum fields when creating a finding so errors point to the invalid input.

5. **Maintainability — `review_triage.py:101–106`**  
   Because `Decision` inherits from `str`, a plain string like `"accepted"` passes the membership check. The string is then stored as the decision, and Markdown rendering fails when it accesses `.value`. Convert supported strings to `Decision` values or reject them consistently at the API boundary.

6. **Performance — `review_triage.py:110–117`**  
   `prioritized()` copies every finding into a tuple. With `open_only=True`, it makes a second tuple before `sorted()` builds its list. Sort directly from the dictionary values, filtering through an iterator when needed. Keep `findings` as a snapshot for callers that request one.

7. **Maintainability — `review_triage.py:138–139`**  
   The empty report check relies on the header always taking exactly four entries in `rows`. If someone adds a subtitle or another header line, the placeholder can silently disappear. Check whether there are findings directly.

## Global Feedback

8. **Security**  
   Decide whether finding messages and rationales should allow Markdown formatting. The current renderer escapes table separators but still allows formatting such as links. Document the intended behavior and test it so AI and human review text is displayed consistently.

9. **Performance**  
   Keep sorting on demand for now. The code has a simple cost of O(n log n) per full sort, which is reasonable for a typical PR. Consider caching only if measurement shows that large reports are rendered repeatedly without changes.

10. **Maintainability**  
    Add tests for equal-severity findings retaining insertion order and for a failed decision leaving the prior finding unchanged. Both behaviors matter to callers and are easy to protect with small tests.