# Functions
## Learning outcomes

*   Write a section of code that can be called with one keyword.
*   Understand the restrictions on variable naming within this code.

## Prerequisites

- [First steps](/first_steps/landing.md)
- [Variables](/variables/landing.md)
- [If statements](/control_flow/if_statements.md)
- [For loops](/control_flow/for_loops.md)

## Application and syntax

At this stage, we should be able to accomplish quite a lot with a Python program. We can see how, as the tasks become more complex, our programs become longer and more repetitive. This makes code more tedious to write and very hard to read or edit.

Thankfully, there is a key building block which can help us organise our code in a more logical way: **the function**. We have encountered functions already. Every time we have used a keyword followed by parentheses `()`, we have been using a function, as with `print("Hello")`, `math.sqrt(2)` or `molecules.append("H2O")`. In this lesson, we will learn how to define our own functions.

A function is an isolated capsule of code where some values are fed in, an operation is carried out, and new values are fed out. Here is the generic syntax:

```Python
def function_name(an_argument):
    Code block, e.g. doing maths on an_argument
    return an_output
```

- ``def`` indicates that we are about to define a new function. 
- ``function_name()`` is what we will use to call our function later on.
- ``(an_argument)`` is the variable that the function will act on, known as the function's <b>argument</b>. It could be a number, string, list, etc., but whatever it is, we need to make sure that we treat it like the correct variable type throughout the main code block. Multiple arguments can be listed if they are separated by commas.
- ``:`` indicates the start of the code that will run whenever we call our function.
- ``Code block`` is a placeholder indicating the main body of the code. It can perform operations using `an_argument` as input data, or even using variables outside the function. All of these operations must be indented in order to belong to `function_name`.
- ``return`` indicates the end of the function.
- ``an_output`` is what this function will yield once it is finished. In a sense, it's the result of the function. For instance, the function `math.sqrt(4)` returns the square root of the argument (so 2). A function is also allowed not to return anything, like the `print()` function, in which case `return` is not followed by anything. Conversely, multiple outputs are also allowed, separated by commas.

Once a function is defined, later in the code, it can be executed by writing its name and inserting any arguments it requires between parentheses. Following the naming above:
```Python
result = function_name(new_argument)
```
Note that we can call this function as many times as we want, with different arguments, and they don't need to be called the same. In the function definition, `an_argument` is a placeholder name, by which we will refer to the inputs in the function body.

Let's look at a real example:
```Python
def atomic_masses_sum(atom_masses):
    """
    Sum all the atomic masses together and return the result.

    Arguments
    ---------
    atom_masses : list of floats
        The masses to be summed.
    
    Returns
    -------
    total_mass : float
        The sum of atomic masses.

    """
    total_mass = 0
    for atom_mass in atom_masses:
        total_mass = total_mass + atom_mass

    return total_mass

water_atomic_masses = [1.008, 1.008, 15.999]
water_total_mass = atomic_masses_sum(water_atomic_masses)

print(f"The total mass of water is {water_total_mass} u.")
```

Note that:
- Below the `def atomic_masses_sum()` line, there is a long multiline comment. A comment directly following a function definition is called a **docstring**. It's an optional inclusion, but it can help someone use the function in the future. For example, in this case, it's helpful to know that `atom_masses` should be a list.
- All of the names inside the function are chosen to be generic (making reference to any molecule). When we call the function, we are using it for the case of water, but we could later call it with a different molecule as an argument.
- The variable `total_mass` is defined within the function, but can't be referenced outside of it (try it!). This is a helpful feature: only the returned variables can be carried into the main body of code. This means, for example, that you can use this function in another program, which already has a function called `total_mass`, and there will be no conflict between the two variables. We say that `total_mass` is within the **namespace** of the function, but not the **namespace** of the program.

Try changing the masses in `water_atomic_masses` and ensure that the result is as you would expect.

```{admonition} Task
Edit the example above so that the function accepts masses in atomic mass units and returns a total mass in grams. The conversion constant is:

$1 \text{u} = 1.66054 \times 10^{-24} \text{g}$
```

<details><summary>Solution</summary>

```Python
def atomic_masses_sum(atom_masses):
    """
    Sum all the atomic masses in atomic massunits together and return the result in grams.

    Arguments
    ---------
    atom_masses : list of floats
        The masses to be summed in u.
    
    Returns
    -------
    total_mass : float
        The sum of atomic masses in g.

    """
    total_mass = 0
    conversion_u_to_g = 1.66054e-24
    for atom_mass in atom_masses:
        total_mass = total_mass + atom_mass

    # convert to g
    total_mass = total_mass * conversion_u_to_g

    return total_mass

water_atomic_masses = [1.008, 1.008, 15.999]
water_total_mass = atomic_masses_sum(water_atomic_masses)

print(f"The total mass of water is {water_total_mass} g.")
```
The key is to make sure that the conversion happens within the function body, so it must be indented. Note how the docstrings were also updated. Previously, the function was unit agnostic, but now it only works properly if we input a particular unit.

It's very important to write good documentation for your code (either as a docstring or as a manual), because using this function incorrectly would return a result without raising an error. It's also possible to write checks within the function to make sure that the input is sensible, but this adds complexity and should only be used as a failsafe to good documentation and useability.

</details>

```{admonition} Task
Write a function which takes an integer as an argument and returns `True` if it is even and `False` if it is odd.

Hint: There are many ways to achieve this, but the modulo (`%`) operator could simplify the solution greatly.
```

<details><summary>Solution</summary>
This is another classic beginner programmer problem.

```Python
def is_even(num):
    """
    Check if a number is even.

    Arguments
    ---------
    num : int
        Number to check
    Returns
    -------
    check: bool
        True if num is even, False otherwise
    
    """
    if num % 2 == 0:
        check = True
    else:
        check = False
    return check

# testing
print(is_even(9))
print(is_even(42))
```

An even number has no remainder when divided by 2, so we can use `% 2` to check the remainder of this division and classify the number.

Once the function is in place, we can check the parity of a number with a single line, instead of needing to write the five lines of code inside the function every time.
</details>

## Summary
- Define a function using the following syntax:
    ```Python
    def function_name(argument_1, argument_2):
        Code
        return a_variable, b_variable
    ```
- Call a function using:
    - General syntax: ``my_function()``. 
    - Assign the output to one or several outputs using: ``result_1, result_2 = my_function(some_argument, other_argument)``.
- Variables defined inside a function body cannot be referenced outside it. 