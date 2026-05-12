# Mathematical operators
## Learning outcomes

*   Use standard Python mathematical operators 
*   Understand the implications of data types on the functioning of operators
*   Access non-standard operators
*   Look for programming help online

## Prerequisites

- [First steps](/first_steps/landing.md)
- [Data types](/variables/data_types.md)
- [Lists](/variables/lists.md)

## Mathematical operations on numbers

Before accessing complicated operations, it's important to learn how to use Python as a simple calculator. There are seven standard mathematical operations that Python can do, though their notation might be slightly different to what you're used to (e.g. &times; is written as ``*`` in Python):

| Operation    | Mathematical Notation | Pythonic Notation |
| -------- | ------- | ------- |
| Addition  | $a + b$ | `a + b` |
| Subtraction | $a - b$ | `a - b` |
| Multiplication | $a \times b$ | `a * b` |
| Division | $a \div b$ | `a / b` |
| Exponent | $a ^ b$ | `a ** b` |
| Modulo | $a \textrm{ mod } b$ | `a % b` |
| Floored Division | $a // b$ | `a // b` |

The modulo and floored division operations may be new to you: 
- Modulo computes the remainder from the division of two numbers. For example, ``5 % 2`` returns ``1``, and ``19 % 4`` returns ``3``. 
- Floored division is the partner to modulo, and returns only the integer part of the division. For example. ``5 // 2`` returns ``2``, and ``19 // 4`` returns ``4``. 

````{admonition} Task
Fill in the gaps to make the following code print `2` twice:

```python
print(97 % □)
print(97 // □)
```
````

<details> <summary>Solution</summary>

There could be several solutions, but you could try:
```python
print(97 % 5)
print(97 // 45)
```

Where `97 = 19 * 5 + 2` and `97 = 45 * 2 + 7`.

</details>

Python can only perform maths on variables of the data type ``integer`` or ``float``. Mathematical operators acted on strings or lists will result in different, exotic, results (more on this later).

A single line of code may have many mathematical operations. In this event, Python will follow the standard order of mathematical operations: you might know this as [BODMAS](https://en.wikipedia.org/wiki/Order_of_operations#Mnemonics). Use round brackets `()` when coding your formulas to avoid ambiguity.

Mathematical operators can be used on variables, numbers, or combinations of both. This becomes useful when a number is very long to write or needs to be repeated many times in code. For example, instead of writing out &pi; or Avogadro's number each time it is used, we can store it at the beginning of the program and only call it by the name you have given it:

``` Python 
pi = 3.141592653589
avogadro = 6.02214e23

# evaluate four times pi times Avogadro's number
product = 4 * pi * avogadro
print(product)
```

Note that to represent standard form, Python uses the symbol `e` instead of <code>&times;10<sup>n</sup></code>.

### Printing mathematical results
There are several ways to display the result of a calculation in Python. As above, we can print a variable, or we could directly evaluate the result inside the print statement, as such:
``` Python 
pi = 3.141592653589
avogadro = 6.02214e23

print(4 * pi * avogadro)
```

These methods are helpful to obtain a quick result, but if the final presentation is important, we can exert more control over the display of numbers by using more advanced features of the f-string:

```Python
mass_C = 12.008 # g mol-1
mass_H = 1.008 # g mol-1
mass_methane = mass_C + 4 * mass_H

# Calling up a variable that has already been calculated
print(f"The mass of methane is {mass_methane:.2f} g mol⁻¹.")
```

```{admonition} Task
Run the code cell above, and guess what the number `2` means in `:.2f` by changing its value.
```

<details> <summary>Solution</summary>

The syntax `:.2f` indicates that the number should be given to 2 decimal places.

</details>

More information on the formatting codes can be found [here](https://docs.python.org/3/library/string.html#formatspec).

```{admonition} Task

Using variables to store the atomic masses of hydrogen, carbon, oxygen, and nitrogen, write a program to calculate the molecular masses of the following species.

1. Ethanol (C<sub>2</sub>H<sub>6</sub>O), doing the calculation inside a print() statement
2. cyclohexanone (C<sub>6</sub>H<sub>10</sub>O), doing the calculation in a variable which you then print
3. Nitrobenzene (C<sub>6</sub>H<sub>5</sub>NO<sub>2</sub>), using an f string

The atomic masses are:
```Python
H = 1.008
C = 12.011
O = 15.999
N = 14.007
```

<details> <summary>Solution</summary>

Your code should look something like this:

```Python
# g mol-1
H = 1.008
C = 12.011
O = 15.999
N = 14.007

print("The mass of ethanol is " , 2 * C + 6 * H + O, "g mol⁻¹." )

mass_cyclohexanone = 6 * C + 10 * H + O
print("The mass of cyclohexanone is " , mass_cyclohexanone, "g mol⁻¹.")

mass_nitrobenzene = 6 * C + H * 5 + N + 2 * O
print(f"The mass of nitrobenzene is {mass_nitrobenzene:.2f} g mol⁻¹.")
```

You should have got the output:
```text
The mass of ethanol is:  46.069 g mol⁻¹.
The mass of cyclohexanone is:  98.145 g mol⁻¹.
The mass of nitrobenzene is: 123.11 g mol⁻¹.
```

We only have to define the masses once, and they can be reused for all three sums.

</details>

```{admonition} Task
The equilibrium constant of an equation

aA + bB ⇌ cC + dD

is given by

$ K_c = \frac{[C]^c \ [D]^d}{[A]^a \ [B]^b} $

For the following equation write a program which calculates the equilibrium constant to 3 decimal places.

2SO<sub>2(g)</sub> + O<sub>2(g)</sub> ⇌ 2SO<sub>3(g)</sub>

Concentrations at equilibrium:<br>
[SO<sub>2</sub>] = 3.0 × 10<sup>−3</sup> mol L<sup>−1</sup><br>
[O<sub>2</sub>] = 3.5 × 10<sup>−3</sup> mol L<sup>−1</sup><br>
[SO<sub>3</sub>] = 5.0 × 10<sup>−2</sup> mol L<sup>−1</sup><br>
```
<details> <summary>Solution</summary>
The numerical answer is <code>79365.079</code>. For a proposed Python code, keep reading:

```Python
# mol L-1
conc_SO2 = 3e-3
conc_O2 = 3.5e-3
conc_SO3 = 5e-2

K_c = conc_SO3**2 / (conc_SO2**2 * conc_O2)

print(f"The equilibrium constant is {K_c:.3f} mol⁻¹ L.")
```
</details>

## Mathematical operations on non-numerical data types

Acting mathematical operators on non-numerical data can give surprising results.

### Maths on strings and lists
Run the two print statements below. 

```Python
print("methyl" + "amine")
print("methyl" * 3)
```

Instead of the mathematical answers 4 and 15, you get this: `methylamine` and `methylmethylmethyl`.

In the first example, the two *strings* have been placed side-by-side. We call this placing *concatenation*. In the second case, the same string has been concatenated three times.

Addition and multiplication also allows us to concatenate lists:

```Python
print([1, 2, 3] + [2, 2, 2])
print([1, 2, 3] * 3)
```

Which results in `[1, 2, 3, 2, 2, 2]` and `[1, 2, 3, 1, 2, 3, 1, 2, 3]`.

````{tip}
This behaviour of strings can lead to dangerous mistakes if you are not careful with your data types. For example, if we try to add numbers together which we don't realise are strings:
```Python
print("3" + "1")
```
We might expect a result of `4` but get `31`. This type of error is especially dangerous because Python hasn't raised an error, so we don't know that something has gone wrong unless we read the result carefully.


If your variables are the wrong data types, you can convert between data types (as long as they are in the correct format) using the functions ``float()``, ``int()``, and ``str()``. This is referred to as casting, e.g. casting a string to an integer value:

```Python
print(int("3") + int("1"))
```

````

### Type errors
More commonly, operations between numerical and non-numerical data don't have any built-in meaning. For example:

```Python

print("beaker" / 2)
```

The code above prints a block of text finishing in:
```text
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

This is a Python error message. The first part tells us the kind of error that has happened: TypeError. What follows saying that the mathematical operator `/` has no defined behaviour when combining a string and an integer.

It's not always easy to decipher Python error message, but fortunately the lines above the error message can help us find the offending line of code. Those lines are called the *Traceback*.

````{admonition} Task
Here are three programs that try to calculate the mean of three numbers. Find the problem in each and suggest a working solution.

**a**
```Python
a = 12.0
b = 5.1
c = 8.5
mean = a + b + c / 3
print(mean)
```
**b**
```Python
a = "12.0"
b = "5.1"
c = "8.5"
mean = (a + b + c)/3
print(mean)
```
**c**
```Python
a = "12.0"
b = "5.1"
c = "8.5"
mean = (int(a) + float(b) + float(c))/3
print(mean)
```
````
<details> <summary>Solution</summary>
In <b>a</b>, the order of operations has been treated poorly, so the answer is incorrect.<br>
In <b>b</b>, the numbers have been turned into strings, and then divided by `3`. Strings can't be divided by integers, which raises `TypeError`.<br>
In <b>c</b>, the strings have been turned into numbers, except Python isn't sure how to turn `"12.0"` into an integer due to the decimal place, even though it is followed by `0`. This raises a new, very common error: `ValueError`.<br>
A simple solution would be:<br>


<pre><code class="language-python">
a = 12.0
b = 5.1
c = 8.5
mean = (a + b + c) / 3
print(mean)
</pre>

</details>

## Non-standard mathematical operators
Python has more specialised mathematical operators stored in external pre-written pieces of code called *libraries*. For example, the `math` library contains more common mathematical tools, like the square root function `sqrt()`.

To use a function from a library, we must first *import* it to our program:

```Python
import math

print(math.sqrt(16))
```

Functions from the `math` library can be accessed by preceding them with `math.`. We can also bypass this by importing only the function we need, with this syntax:

```Python
from math import sqrt

print(sqrt(16))
```

Finally, some library names are abbreviated by convention (and to save on typing). This is the case for the `numpy` library, which also has a `sqrt` function:

```Python
import numpy as np
print(np.sqrt(16))
```

## Seeking programming help online
External libraries allow us to complete complex operations by writing few lines of code. In exchange, we need to learn how a library works based on its documentation which can take time. For example, [here is the documentation page](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html) for `numpy.sqrt`. There is also authoritative documentation for standard Python, like [this section on numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

This kind of documentation is extremely reliable, since it's written by the authors of the library itself. However, it's so comprehensive that it can be hard to understand. Another good source for programming answers is [Stack Overflow](http://stackoverflow.com), which pops near the top of many internet searches. Take [this page](https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python), for example. The top section is a question. Below are answers written by the community and ordered by vote ranking. This means that, even though not every answer is correct, we can dose our trust based on the popularity of the answer, and we can trace back its author.

You may also consider using an AI chatbot to answer your questions. If you do so, you will find that answers to programming questions look extremely similar to the style popularised by Stack Overflow and other such forums for the past few decades. Indeed, Stack Overflow is an influential part of the training set for these chatbots. You might save a bit of time by skipping the online search. In exchange you won't know the provenance of your answer, and therefore won't know how much to trust it. As a general guide, if an answer is hard to find by a standard search engine, a chatbot's answers are more likely to be wrong and made up.

Whatever the source, always check that you understand the code you find before re-using it, and verify the truth of any claims by running some tests on your own computer.

```{admonition} Task
Using a search engine, find a function to operate a Least Squares Fit on a series of data. Get the documentation for the function and a Stack Overflow page explaining its use.
```

<details> <summary>Solution</summary>
Two very popular and reliable Python libraries have least‑squares calculators: <a href="https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html">numpy</a> and <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html">scipy</a>.

<a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html">scipy</a>

Numpy has simpler documentation while scipy has more options. Scroll down both pages to skim the examples of use.

The user "pylang" on Stack Overflow gives <a href="https://stackoverflow.com/a/43623588">a very comprehensive guide</a>. Note that the answer doesn't just focus on the programming but also on the statistical context of the question, which might be useful.
</details>

## Summary 

- Python's basic maths uses the symbols `+`,`-`,`*`,`/`, `**`.
- Use `%`, "modulo", to find the remainder of a division, and ``//``, "floored division" to return the integer part of a division.
- Use order of operations (BODMAS/BIDMAS/PEMDAS) to ensure Python does the correct sum. Use round brackets `()` to remove ambiguity.
- Assign your calculation to a variable to be able to call that value forward later. 
- Inside an f string, use `:.3f` to print your answer to 3 decimal places. Changing the number changes the number of decimal places displayed in the answer.
- For more complex functions, import them from a library or module such as `numpy` or `math`. If you import the whole library, you must reference the library using `modulename.function()`, like in the calculation `answer = math.sin(1)`. 
- Use documentation and programmers' forums for help. Be very suspicious of chatbot answers. Understand and test your answers, wherever they come from.