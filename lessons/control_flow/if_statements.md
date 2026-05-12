# If statements
## Learning outcomes

*   Use comparison operators to write conditions.
*   Use "if statements" to execute code based on these conditions.

## Prerequisites

- [First steps](/first_steps/landing.md)
- [Variables](/variables/landing.md)

## Conditions
### Comparison operators
Our goal in this lesson is to learn to control whether a particular piece of code is executed by Python or is ignored, based on conditions set by us. Since these conditions are binary (execute the code or don't), they should always come down to a boolean value of `True` or `False`.

The essential way to write a condition is to place two values on either side of a *comparison operator*. For example, using the 'lesser than' comparison operator `<`:

```Python
print(1 < 3)
print(3 < 1)
```
you should see the code above output `True`, then `False`.

The common comparison operators you may encounter are the following:

| Operator | Definition | Example |
| --------- | --------- | -------|
| == | is equal to | ``a == b`` |
| != | is not equal to, &ne; | ``a != b`` |
| > | is greater than | ``a > b`` |
| < | is less than | ``a < b`` |
| >= | is greater than or equal to, &ge; | ``a >= b``|
| <= | is less than or equal to, &le; | ``a <= b`` |
| in | the object contains another object | ```a in b``` |

````{tip}
You may use `in` to check whether a value is within a list:
```Python
solvents = ["water", "ethanol", "DMSO"]
print("ethanol" in solvents)
print("methanol" in solvents)
```
You can also use it to check if a string is inside another string:
```Python
solvent = "methanol"
print("anol" in solvent)
print("ate" in solvent)
```
````
````{admonition} Task
In the comparisons in the code below, replace each dash with different comparison operators to get a True output.<br>
```Python
num_nitrogen = 7
num_fluorine = 9

print(num_nitrogen -- num_fluorine)
print(num_fluorine -- num_nitrogen)
print(num_fluorine -- num_nitrogen)
print(num_fluorine -- num_fluorine)
```
````
<details> <summary>Solution</summary>
Here is a set of possible solutions:

```Python
print(num_nitrogen < num_fluorine)
print(num_fluorine > num_nitrogen)
print(num_fluorine >= num_nitrogen)
print(num_fluorine == num_fluorine)
```
</details>

Although most of these comparison operators have an opposite one available, it is sometimes helpful for clarity to invert a condition. To achieve this, precede a comparison by `not`:
```Python
boiling_point = 100.0
temp = 73.3

print("Is the water boiling?", not temp < boiling_point)

```

````{admonition} Task
Read the following comparison statements and predict the output:
```Python
print("Equality")
print(3.14 == 3.15)
print(3.14 == 3.14)
print(3.0 == 3)
print("3.14" == 3.14)
print(3.14 != 3.15)
print(not 3.14 != 3.15)

print("Inequality")
print(3 < 4)
print(-3 > 3)
print(not 5 >= 5)
```

````

Comparisons, and boolean values in general, can be combined together to make more complicated expressions. We achieve this using *boolean operators*

| Operator | Definition | Example (x and y are comparisons) |
| ----- | ---- | ----- |
| and | Both instances must be True to return True, otherwise will return False. | ``x and y`` |
| or | Either instance can be True in order to return True. If both instances are False, will return False. | `` x or y `` |
| not | If the Boolean value of the instance is True, the program will return False. Essentially inverts the logic. | ``not y`` |

This allows us to make combined statements of the form:
```Python
a = 1
b = 2
c = 3
print(a < b and b <= c)
```

These combined statements can start looking quite messy, but we the help of parentheses, we can impose an order of operation and make things neater:
```Python
a = 1
b = 2
c = 3
d = 4
print((a < b or b <= c) and (b < d))
```
Without any parentheses, the default operations is to evaluate all the comparison operators from left to right, and then all of the boolean opeartors from left to right.

````{admonition} Task
What is the logical output of this piece of code?

```Python
w = "tungsten"
print(w == "neon" or w == "iron" or w == "bismuth" or w == "tungsten")
```
````

<details> <summary>Solution</summary>

The answer is `True`. Because each comparison is separated by `or`, only one of them has to be `True` for the overall output to be `True`. Since the last comparison, `w == "tungsten"` is `True`, the overall output is `True`. 
</details>


## If statements and indentation
We are prepared to implement our first condition inside our code. Look at the following example closely and run it in your code editor:
```Python
molecule_a = "CH4"
molecule_b = "CH4"
if molecule_a == molecule_b:
    # This part of the code is run only if the if statement is true
    print("Yes, these molecules have the same formula.")
    print(f"This formula is {molecule_a}.")
print("End of first test.")

if molecule_a != molecule_b:
    # The condition has changed, in this statement
    print("No, these molecules don't have the same formula.")
```
First, note the the syntax of the line `if molecule_a == molecule_b:`. The word `if` is reserved in Python, so should appear in a different colour in your editor. There is then a space and what follows is anything that resolves to a Boolean; here, a comparison. The line must always end with a `:`.

Then, some code appears with 4 leading spaces (which you can write by presing `<Tab>`):
```Python
    # This part of the code is run only if the if statement is true
    print("Yes, these molecules have the same formula.")
    print(f"This formula is {molecule_a}.")
```
The leading spaces are called an *indentation*. Indented code directly following an `if` statement is only executed if the statement is fulfilled. To return to normal operations (where every line of code is executed), we remove the indentation, as in the line `print("End of first test.")`.

Try changing `molecule_b` to a different formula and see how the output changes.

```{admonition} Task
A nickel surface has workfunction 5.08 eV. If a photon incident on the surface has energy greater or equal to this energy, an electron will be liberated from the surface. Write a conditional (`if`) statement to test if a photon of energy 6.17 eV will liberate an electron. If it will, print the energy, and a sentence explaining if an electron has been released.
```
<details> <summary>Solution</summary>

Here is a possible solution:

```Python
workfunction_Ni = 5.08 # eV
photon_energy = 6.17 # eV

if photon_energy >= workfunction_Ni:
    print(f"The photon has energy {photon_energy} eV. It will release an electron from the nickel surface.")
```

Don't forget the colon after the conditional statement, and to indent the `print()` line.

</details>

## Else and elif statements
Often, we want to execute one piece of code if a condition is fulfilled, but a different piece if it is not. This can be achieved by two `if` statements and some careful writing of conditions, but it is easier and clearer to use the `else` keyword.

Here is the same example as earlier but using the `else` keyword:

```Python
molecule_a = "CH4"
molecule_b = "CH4"
if molecule_a == molecule_b:
    # This part of the code is run only if the if statement is true
    print("Yes, these molecules have the same formula.")
    print(f"This formula is {molecule_a}.")
else:
    # Otherwise, this section is run
    print("No, these molecules don't have the same formula.")
```

Try running the code as it is, and then changing `molecule_b`.

The general syntax has us writing `else:` at the same indentation as `if` (so in this case, no indentation) and directly below the `if` block. The `else:` statement is then followed by its own block.

We can be even more precise and combine a condition with an `else` statement, turning it into an `elif` statement:
```Python
molecule_a = "CH4"
molecule_b = "CH4"

# Is this water?
if molecule_b == "H2O":
    print("Molecule B is water.")
# Is molecule B the same as A?
elif molecule_a == molecule_b:
    print("Yes, these molecules have the same formula.")
    print(f"This formula is {molecule_a}.")
else:
    # Otherwise, this section is run
    print("No, these molecules don't have the same formula and molecule B is not water.")
```

The syntax for `elif` is identical to `else` except that it is followed by a boolean. We may chain as many `elif` statements as we want and decide or not to finish them with a catch-all `else`.

Remember, however, that as soon as an `if` or `elif` statement is fulfilled, the indentend block is executed and the rest of the chain of conditions is completely skipped.

````{admonition} Task
Look at these three code-snippets and predict their outputs.

**a**
```Python
x = "CH4"
if x == "CH4":
    print("This compound is methane")
elif x != "NH3":
    print("This compound is not ammonia")
else:
    print("This compound is ammonia")
```

**b**
```Python
x = "H2O"
if x == "CH4":
    print("This compound is methane")
elif x != "NH3":
    print("This compound is not ammonia")
elif x != "H2":
    print("This compound is not hydrogen")
else:
    print("This compound is ammonia")
```

**c**
```Python
x = "H2"
if x != "H2O":
    print("This compound is not water")
if x == "H2":
    print("This molecule is hydrogen")
else:
    print("This compound is not hydrogen")
```
````

<details><summary>Solution</summary>

a) Only the first `print()` statement is executed. Even though the `elif` statement is also True, this is not executed because the first condition has already been met. 

b) The first `if` condition is False, so the program moved on to check the `elif` statement. The first `elif` statement is True, so that print() statement is executed, but the second `elif` statement and the `else` statement are ignored. 

c) Two `if` statements are being used instead of a following `elif`. This means that both conditions are checked, even if the first one is True. Therefore, both statements are executed.

</details>

```{admonition} Task
When doing IR spectroscopy, a peak with low % transmittance corresponds to a strong downward spike on the spectrum (the compound strongly absorbing light). When analysing a particular spectrum, any peaks with transmittance greater than 95% are indistinguishable from background noise, and are ignored. 

Write a Python program that considers a peak transmittance. If the transmittance is not within the 0 to 100% range, print an error message. Otherwise, print the transmittance and whether it is significant or background noise.
```

<details><summary>Solution</summary>
Here is a solution:

```Python
peak_transmittance = 97 # %

if peak_transmittance < 0 or peak_transmittance > 100:
    print("Peak absorbance cannot be less than zero or greater than 100. There may be an error in your instrument.")
elif peak_transmittance >= 95 and peak_transmittance <= 100:
    print(f"The peak has an absorbance of {peak_transmittance}% and can be considered background noise.")
else:
    print(f"The peak has an absorbance of {peak_transmittance}% and can be considered significant.")
```
There could be many ways to order the conditional statements for the same result.
</details>

## Summary
- You can use the following comparison operators: ``==``, ``!=``, `>`, `<`, `>=`, `<=`, and `in`.
- And these boolean operators: `and`, `or`, and `not`.
- You can chain statements together.
- Python evaluates operators in the order: maths and comparisons, then logic. You can clarify your intentions by using round brackets. 
- ``if...elif...else`` is used to create code that only executes if a certain condition is met.
- Use a colon after every `if`/`elif`/`else` condition, and indent any following code that should execute if that condition is met.
- When an `if` statement is True, `elif` and `else` statements directly following it will not execute.
- Use multiple `if` statements if you want every statement checked. Consider how you can minimise the number of `if` statements to have a more efficient and less cluttered code. 