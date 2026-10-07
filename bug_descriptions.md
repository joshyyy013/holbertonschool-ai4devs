# Bug Snippet Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Calculate the total price of shopping cart items
and display it to two decimal places. Display an empty-cart message
when the total is zero.
**Issue Type**: Syntax error.
**Notes**: The if statement is missing a colon, preventing the program
from running. The example cart should total $18.75.

## Bug 2 – bug2.js
**Intended Behavior**: Apply a percentage discount to a price and print
the original price, discount percentage, and final price.
**Issue Type**: Logical error.
**Notes**: The discount is added instead of subtracted. A $100 item
with a 20% discount should cost $80, but the program prints $120.

## Bug 3 – bug3.py
**Intended Behavior**: Calculate and display a student's average score.
If the score list is empty, display a message indicating that no
scores are available.
**Issue Type**: Runtime exception.
**Notes**: An empty list causes division by zero. Alex's average
should be 80.0, while Sam should receive a no-scores message.

## Bug 4 – bug4.js
**Intended Behavior**: Add all numbers in an array and display the sum.
**Issue Type**: Off-by-one error.
**Notes**: The loop runs one iteration beyond the final valid index.
It adds undefined to the total, producing NaN instead of 20.

## Bug 5 – Bug5.java
**Intended Behavior**: Calculate the percentage of completed tasks,
including fractional percentages.
**Issue Type**: Misuse of data types.
**Notes**: Integer division discards the fractional result before it
is assigned to a double. Completing 3 of 8 tasks should produce
37.5%, but the program produces 0.0%.