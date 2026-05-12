# While loops
## Learning outcomes

*   Write pieces of code that run an indeterminate amount of times.
*   Prevent infinite loops.

## Prerequisites

- [First steps](/first_steps/landing.md)
- [Variables](/variables/landing.md)
- [If statements](/control_flow/if_statements.md)
- [For loops](/control_flow/for_loops.md)

## While loop syntax

With `for` loops, we learned how to repeat an operation for a pre-determined amount of iterations. However, in some circumstances, we may want to keep repeating until certain conditions are met. The solution for this, is the `while` loop. Here is the generic syntax:

```Python
while condition:
    some action
```

- `while` initiates the loop.
- `condition` should be replaced with an expression that amounts to a Boolean. If the Boolean is `True`, the loop will repeat. If it ever becomes `False`, the loop stops.
- `some action` is to be replaced by whatever action you want to repeat, just like a `for` loop.

For example:
```Python
n_protons = 1

while n_protons < 6:
    print(f"The number of protons is {n_protons}.")
    n_protons = n_protons + 1 # add 1 to n_proton
```

Note how the number 6 never appears because as soon as `n_protons` becomes `6`, the condition is not fulfilled and the while loop stops. Exchange the order of the last two lines. Check the output and ensure that it makes sense.

```{admonition} Task
Remove the `n_proton = n_proton + 1` line of the example above and run the code. Your output should be printing line after line without ever stopping. To break out of this infinite loop, click on the output window, then press `Ctrl+.` and click "Yes".
```

This example showed how small errors can accidentally cause infinite loops, which keep your computer busy until they are solved. `while` loops are the primary cause of infinite loops in programming, but thankfully most problems can be resolved with a safer `for` loop in Python.

```{admonition} Task
The Fibonacci sequence is the series of numbers starting with 0 and 1, where each new number is the sum of the two previous ones:

0, 1, 1, 2, 3, 5, 8, ...

Write a program which prints out every number of the Fibonacci sequence and stop as soon as you exceed 1000, using a `while` loop.

Hint: You will need to define two variables. One will contain the penultimate Fibonacci number at the current iteration(starting at `0`). The other will contain the final number at the current iteration (starting at `1`).
```

<details><summary>Solution</summary>

This is a hard task but a classic exercise for beginner programmers.
```Python
# initiate Fibonacci sequence
fibo_old = 0 # penultimate number
fibo_new = 1 # current final number

# set ending condition
while fibo_new < 1000:
    # calculate the new number
    new_sum = fibo_new + fibo_old
    # update the penultimate number
    fibo_old = fibo_new
    # update the new final number
    fibo_new = new_sum
    print(fibo_new)
```
This is an example of a task that is more at home in a `while` loop than a `for` loop. We can't expect to know how long the loop will be (or we'd already know the answer), so `while` is our best bet. It's possible to construe a `for` loop with a careful `break` statement to achieve the same task, but it would be longer to write and less clear to read.

If you want to challenge yourself, add an `if` statement so that only the odd Fibonacci numbers are printed.
</details>

## Summary

- The syntax of a ``while`` loop is: ``while condition:``, and the code within the loop is on the lines immediately following it, indented using ``<tab>``.
- `while` loops are liable to looping infinitely if their condition never becomes `False`.
- `while` loops can be combined with `if` statements and `for` loops by using indentation.
