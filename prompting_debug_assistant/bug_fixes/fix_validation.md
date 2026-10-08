# Fix Validation

## Testing Environment

The corrected snippets were tested locally on Windows.
Python snippets were run through Anaconda Prompt.
JavaScript snippets were run using Node.js.
The Java snippet was compiled with javac and run using java.

## Bug 1 – bug1_fixed.py

- **Input**: Prices [10.50, 5.25, 3.00].
- **Expected Output**: Total: $18.75
- **Actual Output**: Total: $18.75
- **Result**: PASS.
- **Fix Applied**: Added the missing colon to the if statement.
- **Manual Tweaks**: No additional code changes.

**Test Command**:
    python bug1_fixed.py

## Bug 2 – bug2_fixed.js

- **Input**: Price 100, discount 20%.
- **Expected Output**:
    Original price: $100.00
    Discount: 20%
    Final price: $80.00
- **Actual Output**:
    Original price: $100.00
    Discount: 20%
    Final price: $80.00
- **Result**: PASS.
- **Fix Applied**: Subtracted the discount from the original price
  instead of adding it.
- **Manual Tweaks**: None.

**Test Command**:
    node bug2_fixed.js

## Bug 3 – bug3_fixed.py

### Test 1: Non-empty scores

- **Input**: Alex, scores [70, 80, 90].
- **Expected Output**: Alex's average: 80.0
- **Actual Output**: Alex's average: 80.0
- **Result**: PASS.

### Test 2: Empty scores

- **Input**: Sam, scores [].
- **Expected Output**: Sam has no scores available.
- **Actual Output**: Sam has no scores available.
- **Result**: PASS.

**Fix Applied**: Checked for empty scores before calculating and
printing the average. Used normal division `/` to preserve fractional
averages.

**Manual Tweaks**: Replaced floor division `//`, which had been
introduced during the initial correction, with normal division `/`.

**Test Command**:
    python bug3_fixed.py

### Test 3: Fractional average

- **Input**: Taylor, scores [70, 81].
- **Expected Output**: Taylor's average: 75.5
- **Actual Output**: Taylor's average: 75.5
- **Result**: PASS.
- **Purpose**: Confirms that normal division preserves fractional averages.

## Bug 4 – bug4_fixed.js

- **Input**: Numbers [2, 4, 6, 8].
- **Expected Output**:
    Numbers: 2, 4, 6, 8
    Total: 20
- **Actual Output**:
    Numbers: 2, 4, 6, 8
    Total: 20
- **Result**: PASS.
- **Fix Applied**: Changed the loop condition from
  `i <= numbers.length` to `i < numbers.length`,
  preventing access beyond the last valid index.
- **Manual Tweaks**: None.

**Test Command**:
    node bug4_fixed.js

## Bug 5 – bug5_fixed.java

- **Input**: 3 completed tasks, 8 total tasks.
- **Expected Output**:
    Completed tasks: 3
    Total tasks: 8
    Completion: 37.5%
- **Actual Output**:
    Completed tasks: 3
    Total tasks: 8
    Completion: 37.5%
- **Result**: PASS.
- **Fix Applied**: Cast completed to double before division:
  `double percentage = ((double) completed / total) * 100;`
- **Manual Tweaks**: Corrected the typo `nocompleted` to `completed`.
  Matched the public class name to the submission filename
  `bug5_fixed.java` by naming the class `bug5_fixed`.

**Test Commands**:
    javac bug5_fixed.java
    java bug5_fixed

**Compilation Result**: Compilation completed without errors.

## Summary

All five corrected snippets produced the expected outputs for the
documented test cases. Bug 3 also handled an empty scores list
without raising an exception.