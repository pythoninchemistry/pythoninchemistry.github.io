# For loops
## Learning outcomes

*   Write pieces of code that run multiple times (loops).
*   End loops in a predictable way.
*   Make predictable changes to each iteration of the code.

## Prerequisites

- [First steps](/first_steps/landing.md)
- [Variables](/variables/landing.md)
- [If statements](/control_flow/if_statements.md)

## For loop over a list
### Basic syntax

When programming, we may want to repeat the same (or almost the same) operation hundreds of times. Instead of writing hundreds of line of code, our preferred solution in Python is the `for` loop.

We will start with the most common scenario: you have a list of values and want to act on each element of the list.

Just like with ``if`` statements, ``for`` loops require specific syntax:

```Python
for discrete_variable in list_of_values:
    some action
```

- `for` indicates that we will begin a loop.
- `discrete_variable` is a new variable we are defining, which will adopt each element of the list one by one. At every repetition of the loop, it will change its value to the new element. The technical term for these stand-in variables is a *discrete variable*.
- `in list_of_values` indicates that we want to repeat the action in the loop once per item in the list `list_of_values`.
- `:` signals the beginning of the loop.
- `some action` is to be replaced by whatever action you want to repeat. It can take multiple lines but they all have to be indented. When the code is no longer indented, the loop is over.

Here is an example:

```Python
molecules = ["H2", "H2O", "CH4"]

for mol in molecules:
  print(mol)
```

Run the code and make sure you understand each line. The most exotic feature is the discrete variable `mol`. Notice that we can use `mol` within the `for` loop for printing, even though we never defined it in the usual way (`mol = "H2"`). This is because it is defined within the opening line of the loop.

Try adding or removing elements in `molecules` and see what happens.

````{admonition} Task
Complete the following code so that each element of the list is printed within an f-string.

```Python
atomic_masses = [1.008, 4.003, 7.0]

print("These are the first atomic masses of the periodic table:")

for -- in --:
    print(f"Mass: {--} u")

```
````

<details> <summary>Solution</summary>

```Python
atomic_masses = [1.008, 4.003, 7.0]

print("These are the first atomic masses of the periodic table:")

for atomic_mass in atomic_masses:
    print(f"Mass: {atomic_mass} u")

```
Here, `atomic_masses` is the list, so must appear after `in`. The discrete variable `atomic_mass` could be named anything, but it needs to be the same name used within the loop. Even though the discrete variable is only going to be used within this loop, it's still good practice to give it a descriptive name.
</details>

### Multi-line for loops

We can do more than just printing inside a `for` loop. All of the Python we have learned so far applies. What follows is a typical piece of Python code (a.k.a. a *programming pattern*) for generating new lists. Here, we know some pressures in mmHg and want to turn them all into bar.

```Python
# a list of known pressures in mmHg
pressures_mmHg = [2945.01, 1671.43, 908.56, 625.3]

# an empty list which we want to fill up with the unknown pressures in bar
pressures_bar = []

# loop over the pressures in mmHg
for pressure_mmHg in pressures_mmHg:
    # calculate the pressure in bar
    new_pressure_bar = pressure_mmHg / 750.06

    # as a sanity check, print the new value
    print(new_pressure_bar)

    # append the new presure to our target list
    pressures_bar.append(new_pressure_bar)

# outside of the loop, we check the result
print(pressures_bar)
```

In a final version of the code, we would remove the sanity check. Look at the output and make sure that you can match up each printed line to a print statement in the code. Note how the indented print statement is used multiple times while the unindented one happens only once.

```{admonition} Task
Write a `for` loop which prints the square of each number from 1 to 4.
```

<details> <summary>Solution</summary>

```Python
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number**2)

```
Again, `number` could be named anything as long as we use that name correctly later in the `for` loop. In many cases, you will find discrete variables named `i` or `j`, inspired by indices of mathematical equations. Try to resort to this only if the meaning of the variable is so abstract that giving it a non-mathematical name would be confusing.
</details>

### For loops and if statements

We can use our knowledge from the last lesson to combine `if` and `for`. Look at this example which picks out molecular formulas containing carbon:

```Python
molecules = ["N2", "H2", "CH3OH", "H2O", "CH4"]

# loop over all molecules
for mol in molecules:
    print(f"Checking molecule: {mol}...")
    if "C" in mol:
        print(f"{mol} contains carbon!")
    print(f"Finished checking molecule: {mol}.")

```

The most striking feature of this code is the indentation. Notice how, to insert an `if` block, we had to indent a line twice. This ensures that it is within the `if` statement, which itself is contained within the `for` loop (since the `if` line is indented once).

We say that the `if` statement is *nested* within the `for` loop. We can nest however many expressions we need, which unlocks the huge algorithmic power of programming. Using indentation for nesting is unique to Python and can be hard to get your head around, so try adding some `print()` statements to the code above at different levels of indentation to verify that you understand how everything works.

```{admonition} Task
Modify the example above to generate a list of molecules containing carbon by using `append()` inside the `for` loop.
```

<details> <summary>Solution</summary>

```Python
molecules = ["N2", "H2", "CH3OH", "H2O", "CH4"]
# make an empty list
organic_molecules = []

# loop over all molecules
for mol in molecules:
    print(f"Checking molecule: {mol}...")
    if "C" in mol:
        print(f"{mol} contains carbon!"")
        organic_molecules.append(mol)
    print(f"Finished checking molecule: {mol}.")

print("The molecules containing carbon are:")
print(organic molecules)
```
You only need to define an empty list before the `for` loop, and then append `mol` inside. The difficulty is to place the `append()` call at the right indentation so that it happens within the `for` loop (first indentation) and only if the condition is fulfilled (second indentation). 
</details>

### Breaking and continuing loops
You may sometimes want to stop a loop given a condition. This typically happens if you are iterating over a long list and obtain the result you want before the end. In this scenario, we can use the keyword `break`.

```Python
molecules = ["H2O", "HCN", "CO2", "NH3", "CH3"]

for formula in molecules:
    if formula == "CO2":
        break
    print(formula)
```
You should see that only the two first formulas are printed. The order of operation of the code is as follows:
1. The loop is initiated and `formula` becomes `"H2O"`.
2. The `if` condition is not fulfilled, so the `break` line is skipped.
3. `formula` is printed.
4. `formula` becomes `"HCN"` and the same loop repeats.
5. `formula` becomes `"CO2"`.
6. The `if` condition is fulfilled, so we proceed to the double-indented code.
7. `break` is encountered, and the whole `for` loop stops.

Modify the `molecules` list and ensure that what is printed matches your understanding of `break`.

A similar keyword is `continue`, doesn't end the loop but stops the current iteration and skips to the next one:
```Python
molecules = ["H2O", "HCN", "CO2", "NH3", "CH3"]

for formula in molecules:
    if formula == "CO2":
        continue
    print(formula)
```
Try to follow the order of operation of this piece of code just as we did for `break` above.

## For loops over multiple lists
### Nested loops
Just as we can place an `if` statement inside a `for` loop, we can also place a `for` loop inside another. Let's say we want to calcualte the left-hand-side of the ideal gas equation $pV$ for a range of pressures $p$ and volumes $V$.

```Python
# define the ranges of pressure and volume
p_range = [0.980e5, 1.021e5, 1.044e5, 1.101e5] # Pa
V_range = [2.3, 3.1, 5.6] # metres cubed

# loop over 
for pressure in p_range:
    for volume in V_range:
        product = pressure * volume
        print(f"{pressure} Pa x {volume} m^3 = {product} J")
```

Note the order in which each result appears. A first value for `pressure` is adopted. We then encounter the second `for` loop, which will loop over every `volume` value before `pressure` changes to its second value. Try to exchange the first two lines of the program and correct their indentation. Check that the output changes as you would expect.

```{admonition} Task
Make a script which prints out every integer coordinate in a 5 x 5 grid, and its distance from the origin. Use a nested `for` loop to automatically generate each coordinate pair.

The distance of a coordinate $(x,y)$ from the origin is $r = \sqrt{x^2 + y^2}$.
```

<details> <summary>Solution</summary>

```Python
import math # for the square root

# integer numbers from 0 to 5
integers = [0, 1, 2, 3, 4, 5]

for x_coord in integers:
    for y_coord in integers:
        distance_from_origin = math.sqrt(x_coord**2 + y_coord**2)
        print(f"The coordinate ({x_coord}, {y_coord}) is {distance_from_origin} away from the origin.")
```
Note how, in this case, we could use `integers` as the list for both coordinates, and therefore both `for` loops. This is because the x and y values each take the same values to make a square grid. If the grid was rectangular, or had different spacing in each coordinate, we would need to define two different lists, not just `integers`.
</details>

### The zip function
We have now seen situations where we can combine one or two lists for nested iterations. Sometimes, though, we may be called to use values on multiple lists at the same time but not in every combination. For instance, in our ideal gas example, we may have three pressures and three volumes that each go in pairs (that is, the first pressure multiplies the first volume, the second pressure the second volume, etc.). In this scenario, we can use the `zip()` function as follows:

```Python
# define the ranges of pressure and volume
p_range = [0.980e5, 1.021e5, 1.044e5] # Pa
V_range = [2.3, 3.1, 5.6] # metres cubed

# loop over each pressure/volume pair
for pressure, volume in zip(p_range, V_range):
    product = pressure * volume
    print(f"{pressure} Pa x {volume} m^3 = {product} J")
```

Note the different syntax in the `for` line. We have defined two discrete variables separated by a comma. Where the list would be, there is a `zip()` function, whose arguments are the lists. `zip()` works with as many arguments as we need, as long as each of them has the same length (it wouldn't do to try to calculate pairs of pressure and volume if there were different numbers of them).

````{admonition} Task

A Cartesian coordinate, $(x, y)$ can be rotated clockwise to a new position $(x', y')$ by an angle $\theta$ around the origin using the following formulae:

$ x' = x \ cos(\theta) + y\ sin(\theta) $ <br>
$ y' = -x \ sin(\theta) + y\  cos(\theta) $

A group of argon atoms have the following x and y coordinates in angstrom:

```Python
x_coords = [1.12, -6.99, -9.48, 8.89, -6.28, -4.98, 6.27, 7.35, 0.87, -9.50]
y_coords = [-1.87, 1.43, 6.38, 4.44, -0.12, -1.56, -8.71, -3.78, -0.31, -1.24]
```

By zipping together these lists and iterating through with a `for` loop, rotate these coordinates by 30 $\degree$ clockwise around the origin. Store the new values in two new lists.

**Hint**: Remember that you can access `sin()` and `cos()` functions using the Python module `math`, and that these modules take values in *radians*, not degrees. 30 $\degree$ represents $\degree/6$ rad.
This is the answer you should get:

```Python
Rotated x coordinates:  [0.03494845223857146, -5.338517572453227, -5.019920827876479]
Rotated y coordinates:  [-2.1794675050769006, 4.733416327411747, 10.265242076144718]
````

<details><summary>Solution</summary>

```Python
import math

# Coordinates to be rotated
x_coords = [1.12, -6.99, -9.48]
y_coords = [-1.87, 1.43, 6.38]

# Define the angle of rotation in radians
angle = math.pi / 6

# Empty lists to store the rotated coordinates
rot_x_coords = []
rot_y_coords = []

# Loop through the original coordinates, zipping x and y together
for x, y in zip(x_coords, y_coords):
    # Rotate the coordinates by the specified angle
    new_x = x * math.cos(angle) + y * math.sin(angle)
    new_y = -x * math.sin(angle) + y * math.cos(angle)

    # Append the new coordinates to the respective lists
    rot_x_coords.append(new_x)
    rot_y_coords.append(new_y)

print("Rotated x coordinates: ", rot_x_coords)
print("Rotated y coordinates: ", rot_y_coords)
```

Here, we used:

- The design pattern of defining empty lists ahead of a loop before appending.
- The `math` library to access trigonometric functions and `math.pi`.
- The `zip()` function to access each `x`/`y` pair instead of every combination of `x` with `y`.

</details>

## For loops over ranges
### The range function
Sometimes, we may wish to repeat an operation but linked to any pre-existing list. In these cases, Python provides us with the `range()` function. This function can be used in place of a list in a `for` loop, and returns numbers:
```Python
for i in range(3):
    print(i)
```
This allows us to print the numbers 0, 1, and 2 without needing to define the list `[0, 1, 2]`. Note that `range()` starts counting from `0` and reaches one less than the argument (here, `2` is one less than `3`).

````{admonition} Task

You can exert more control over range by giving it more arguments. Run the following code and deduce what the roles of the arguments are in `range(3,9,2)`.

```Python
for j in range(3, 9, 2):
    print(j)
```
````

<details><summary>Solution</summary>
The output should be `3`, `5`, and `7`. We are starting the range at `3` and increasing the value in steps of `2` before stopping just before the value `9`. The generic syntax is:

```Python
for i in range(start, end, step):
    print(i)
```
</details>

### The enumerate function
Finally, we sometimes want to loop over a list while still having access to the number index of the current position, as with `range()`. In this case, we can use `enumerate()`.

```Python
atom_names = ["H", "He", "Li", "Be"]

for ind, atom in enumerate(atom_names):
    print(atom, "is at position" , ind, "in the list")
```
Just as with `zip()`, we are defining two discrete variables. The first is the index (`ind`), which will take integer values starting at 0 and increasing by 1 every loop. The second (here, `atom`) is the usual element of the interested list, just as in our first `for` loop examples. Instead of following `in` by a list, we call the `enumerate()` function, and give it a list as an argument.

Having access to the position of an element in a list can be useful if, for example, we wish to treat elements differently based on their position.

````{admonition} Task
Complete the following code so that every wavelength is printed except for the first and last:

```Python
wavelengths = [300, 400, 500, 600, 700, 800]

for ind, wavelength in enumerate(wavelengths):
    if ---:
        print(wavelength)
```
````

<details><summary>Solution</summary>

```Python
for ind, wavelength in enumerate(wavelengths):
    if ind > 0 and ind < 5:
        print(wavelength)
```
Here, we need to be careful with the condition in our `if` statement. Many solutions would be possible. Remember that the index counts from 0.

</details>

## Summary

- The syntax of a ``for`` loop is: ``for i in list:``, and the code within the loop is on the lines immediately following it, indented using ``<tab>``.
- You can nest `if` statements and other `for` loops inside `for` loops. For each degree of nesting, an added indentation is needed.
- ``break`` will end the loop when encountered.
- ``continue`` will move the program onto the next iteration of the loop.
- When iterating through two related lists of the same size, you can associate them pairwise using the ``zip()`` function. The syntax is: ``for i, j in zip(list1, list2):``. The two lists MUST be the same dimensions.
- You can assign each item in a list an index value using the ``enumerate()`` function. The syntax is: ``for index, value in enumerate(list):``.
- Use the ``range()`` function to iterate a set number of times. The syntax is: ``for i in range(start, stop, step))``, or, with just one argument, `for i in range(stop)`.
