# AI Debug Log

## Approach

I used an AI assistant to explain each bug and suggest a fix.
I applied and tested the fixes in a separate `test_fixes` folder,
preserving the original buggy snippets.

Prompt:
"This code throws an error / doesn't behave as expected.
Can you identify and explain the issue and how to fix it?"

## Bug 1 – bug1.py

**AI Diagnosis**: The statement `if total > 0` is missing a colon.
Python requires a colon before the indented body of an if statement.
The missing colon causes a SyntaxError.

**Suggested Fix**:
```python
if total > 0:
```

**Alternative Fixes Tested**: None.

**Test Command**:
```bash
python bug1.py
```

**Actual Output**:
```text
Total: $18.75
```

**Result**: The corrected program runs and displays the expected total.

## Bug 2 – bug2.js

**AI Diagnosis**: The discount is added to the original price instead
of subtracted. This increases the price rather than reducing it.

**Suggested Fix**:
```javascript
const finalPrice = price - discount;
```

**Alternative Fixes Tested**: None.

**Test Command**:
```bash
node bug2.js
```

**Actual Output**:
```text
Original price: $100.00
Discount: 20%
Final price: $80.00
```

**Result**: The program correctly applies a 20% discount to $100,
producing a final price of $80.

## Bug 3 – bug3.py

**AI Diagnosis**: The original calculation divides by the length of
the scores list. An empty list has length zero, causing a
ZeroDivisionError.

During correction, `//` was used for division. This performs floor
division and loses fractional averages. Normal division `/` preserves
the fractional result.

**Suggested Fix**: Use normal division with an empty-list fallback:
```python
average = total / len(scores) if scores else 0
```

Check for empty scores before calculating and printing the average:
```python
def print_average(student, scores):
    if not scores:
        print(f"{student} has no scores available.")
        return

    average = calculate_average(scores)
    print(f"{student}'s average: {average:.1f}")
```

**Alternative Fixes Tested**: No separate alternative fix was tested.
The supplied terminal results show two runs with the same output.

**Test Command**:
```bash
python bug3.py
```

**Actual Output**:
```text
Alex's average: 80.0
Sam has no scores available.
```

**Result**: The program displays Alex's expected average and handles
Sam's empty scores list without an exception. These inputs do not
verify fractional averages; a test such as `[70, 81]` would be needed
to confirm an average of 75.5.

## Bug 4 – bug4.js

**AI Diagnosis**: The condition `i <= numbers.length` allows the loop
to access an index beyond the end of the array. That access returns
undefined, and adding it to the total produces NaN.

**Suggested Fix**:
```javascript
for (let i = 0; i < numbers.length; i++) {
    total += numbers[i];
}
```

**Alternative Fixes Tested**: None.

**Test Command**:
```bash
node bug4.js
```

**Actual Output**:
```text
Numbers: 2, 4, 6, 8
Total: 20
```

**Result**: The loop visits only valid indexes and calculates the
expected total of 20.

## Bug 5 – Bug5.java

**AI Diagnosis**: Both operands in `completed / total` are integers,
so Java performs integer division. For 3 completed tasks out of 8,
the division produces 0. Assigning that result to a double does not
recover the fractional part.

**Suggested Fix**: Cast completed to double before dividing:
```java
double percentage = ((double) completed / total) * 100;
```

**Alternative Fixes Tested**: None.

**Issues Encountered During Testing**:
- The initial compilation reported that the public class `Bug5`
  must be in a file named `Bug5.java`. The filename was corrected
  to match the class name, including capitalization.
- The expression accidentally used `nocompleted`, which is not a
  declared variable. It was corrected to `completed`.
- These were filename and typing corrections, not alternative
  solutions to the integer-division bug.

**Test Commands**:
```bash
javac Bug5.java
java Bug5
```

**Actual Output**:
```text
Completed tasks: 3
Total tasks: 8
Completion: 37.5%
```

**Result**: After correcting the compilation issues, the program ran
and displayed the expected completion percentage of 37.5%.