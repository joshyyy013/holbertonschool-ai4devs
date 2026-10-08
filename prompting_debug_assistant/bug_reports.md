# Structured Bug Reports

## Bug Report – bug1.py

- **Fixed File**: bug_fixes/bug1_fixed.py
- **Summary**: The program could not run because of a syntax error.
- **Root Cause**: The statement `if total > 0` was missing the
  colon required by Python.
- **Resolution — AI Suggestion**: Change the statement to
  `if total > 0:`.
- **Resolution — Manual Edits**: Applied the suggested correction.
  No additional code changes were needed.
- **Lessons Learned**: Python compound statements require a colon.
  Syntax errors must be resolved before program behaviour can be tested.

## Bug Report – bug2.js

- **Fixed File**: bug_fixes/bug2_fixed.js
- **Summary**: Applying a discount increased the price instead of
  reducing it.
- **Root Cause**: The calculation used `price + discount`.
- **Resolution — AI Suggestion**: Replace the calculation with
  `price - discount`.
- **Resolution — Manual Edits**: Applied the suggested correction.
  No additional code changes were needed.
- **Lessons Learned**: Code can run without exceptions and still
  produce incorrect results. Compare outputs against independently
  calculated expectations, such as $80 for a 20% discount on $100.

## Bug Report – bug3.py

- **Fixed File**: bug_fixes/bug3_fixed.py
- **Summary**: Calculating an average for an empty scores list
  caused a division-by-zero exception.
- **Root Cause**: The original function divided the total by
  `len(scores)` without checking whether the list was empty.
  During correction, using `//` also introduced floor division,
  which would discard fractional averages.
- **Resolution — AI Suggestion**: Check for empty scores in
  `print_average` and display a no-scores message. Use `/` for
  normal division.
- **Resolution — Manual Edits**: Applied the empty-list check,
  added an empty-list fallback in `calculate_average`, and replaced
  the initially used `//` with `/` following AI feedback.
- **Lessons Learned**: Test both normal inputs and empty collections.
  Include fractional values when testing averages, because a
  whole-number average cannot reveal a floor-division error.
  An empty dataset should not be presented as a genuine zero average.

## Bug Report – Bug5.java

- **Fixed File**: bug_fixes/bug5_fixed.java
- **Summary**: The program reported 0.0% completion for 3 out of
  8 completed tasks instead of 37.5%.
- **Root Cause**: Both operands in `completed / total` were integers.
  Java performed integer division before assigning the result
  to a double.
- **Resolution — AI Suggestion**: Cast completed to double before
  division:
  `double percentage = ((double) completed / total) * 100;`.
- **Resolution — Manual Edits**: Applied the cast, corrected the
  accidental variable typo `nocompleted` to `completed`, and matched
  the public class name to the filename. The submitted file and
  class were named `bug5_fixed.java` and `bug5_fixed`.
- **Lessons Learned**: A double destination does not change how
  an integer expression is evaluated. Convert an operand before
  division. Java public class names must match their filenames,
  including capitalization.

## Bug Report – bug4.js

- **Fixed File**: bug_fixes/bug4_fixed.js
- **Summary**: Summing the array produced NaN instead of 20.
- **Root Cause**: The loop condition `i <= numbers.length` allowed
  access to one index beyond the array. This returned undefined,
  which produced NaN when added to the total.
- **Resolution — AI Suggestion**: Change the condition to
  `i < numbers.length`.
- **Resolution — Manual Edits**: Applied the suggested correction.
  No additional code changes were needed.
- **Lessons Learned**: Array indexes start at zero and end at
  length minus one. Check loop boundaries carefully; an invalid
  JavaScript array access can return undefined without immediately
  throwing an exception.