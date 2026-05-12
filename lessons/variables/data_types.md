# Data types

## Learning Outcomes

* Understand how to print basic outputs in Python.
* Understand how to identify and verify the type of a variable.

## Prerequisites

* [First steps](/first_steps/landing.md)

## What is a variable?

A variable is a place where some information can be held in the code and can be
used in many different ways within a programme. You can create a variable like
this:

```python
atomic_number = 2
```

where the word on the left of the `=` sign is the *name* of the variable and
whatever is on the right is its *value*.

## Print function

To reveal the value stored in a variable, you can use the `print()` function.
For example:
```python
atomic_number = 2
print(atomic_number)
```

```{admonition} Task
Change the value of `atomic_number` to 3 and print the new value.
```

<details><summary>Solution</summary>
Change the code to:

```python
atomic_number = 3
print(atomic_number)
```
</details>

## Naming of variables

There are few rules you must follow when naming a variable.

### Variable name requirements

*   Variables can only start with a letter or underscore (\_) character and may
    not start with a number.
*   Can only include upper and lowercase letters, numbers and the underscore
    character (A-z, 0-9, and _ ).
*   Names must not be a [Python keyword](https://docs.python.org/3/reference/lexical_analysis.html#keywords).

You do not need to memorise all Python keywords. A good code editor will
highlight reserved keywords in a different colour to alert you.

### Good variable naming

Choosing the right variable name will allow your code to be easier to understand
for you and future programmers interacting with your code. Good names increase
clarity, therefore they should be:

#### Descriptive
The name gives a hint about what the value means.

| Bad example   | Good example       |
|---------------|--------------------|
| `number = 12` | `atomic_mass = 12` |

#### Short
The name is brief without compromising clarity.

| Bad example                                | Good example          |
|--------------------------------------------|-----------------------|
| `molecular_mass_of_protium___oxide = 18.015` | `water_mass = 18.015` |

Note that if your programme distinguishes between different kinds of masses or
between light and heavy water, the former choice could be the correct one.

#### Consistent
The name follows a convention to avoid multiple spellings of one same thing. The
preferred convention for variable names in Python is called `snake_case`, where
all letters are lower-case and words can be separated by underscore characters
(`_`).

| Bad example                | Good example                |
|----------------------------|-----------------------------|
| `roomTemperature = 298.15` | `room_temperature = 298.15` |

Sometimes, descriptiveness, shortness, and consistency come into conflict, and
it is up to you to decide which one should win out for the best clarity. As an
exercise, think of a good variable name for the molecular mass of the last
molecule you synthesised. For example:

```python
CuSO4_mass = 132.16
```

```{admonition} Task

Can you tell what naming rule is broken in the variable name above?

```

<details><summary>Solution</summary>

Following `snake_case` conventions, all the letters should be lowercase, so the
variable should be called `cuso4_mass`. However, capitalisation is meaningful in
Chemistry, and we would like to distinguish between copper (Cu) and carbon and
uranium (CU).

In our context, it is therefore wise to break the `snake_case` convention in
favour of the Chemistry convention.

</details>


## Types

Variables are classified in terms of their *type*. This is an indicator of the
kind of value stored inside, such as a number or a word.



We can check the type of the variable `atomic_number` like this:

```python
atomic_number = 2
print(type(atomic_number))
```

This code prints out the result: `<class 'int'>` The important part of this line is the word `int`. As we will see next, this stands for *integer*, which is the type of `1`.

Here is a summary of the most common variable types:

| Name    | Abbreviation | Example  | Explanation                   |
|---------|--------------|----------|-------------------------------|
| Integer | `int`        | `3`      | A whole number                |
| Float   | `float`      | `3.14`   | A number with a decimal point |
| Boolean | `bool`       | `True`   | Either `True` or `False`      |
| String  | `str`        | `"acid"` | Any kind of text              |

What follows is an explanation for each one. For each type, there is a code snippet which shows how the variable is assigned, the variable is printed, and the type of variable is printed.

```{admonition} Task
For each of the following data types, run the code block in Spyder, and then modify the value of the variable to a new value of your choice to ensure that it remains of the type you expect.
```

### Numbers
#### Integer

An integer (`int`) is any whole number. Integers can also be negative.

```python
ionic_charge = -2
print(ionic_charge)
print(type(ionic_charge))
```

#### Float

A float (`float`) is any number where you have a decimal place. For very big or very small numbers, you can use scientific notation to write floats. For example, for Avogadro's number, you can write `6.023e23`.

```python
nitrogen_mass = 14.0067
print(nitrogen_mass)
print(type(nitrogen_mass))

electron_charge = 1.602e-19
print(electron_charge)
print(type(electron_charge))
```

### Boolean

Boolean (`bool`) can only have the value `True` or `False`.

```python
boiling = True
print(boiling)
print(type(boiling))
```

### Strings

A string (`str`) stores a sequence of text characters. They can be used to write
words or sentences. You signify what characters are stored by writing quotation
marks either side of the characters, like `'this'` or `"this"`.

```python
molecule_name = "acetaldehyde"
print(molecule_name)
print(type(molecule_name))
```

There is another way of writing strings which allows you to combine them with
other variables of any type. We call this an _f-string_. Before the quotation
mark, include the letter `f`, then within the string, you can include other
variables enclosed in curly brackets `{}`.

```python
atomic_mass = 14.0067
element_name = "nitrogen"
heavier = True

result_string = f"The atomic mass of {element_name} is {atomic_mass}.\nHeavier than carbon: {heavier}."
print(result_string)
```

The previous f-string used an additional trick. Including `\n` in a string
indicates a line-break.


````{admonition} Task
The following piece of code only works correctly if `mass` is defined as a
number:

```Python
mass = "35"
double_mass = mass*2
print(f"Two times {mass} kg makes {double_mass} kg.")
```

Run this code, find what is wrong with it and fix it.
````

<details><summary>Solution</summary>
The number 35 was multiplied incorrectly. This is
because <code>mass</code> was defined as a string, since the number
<code>"32"</code> was written with quotation marks. If you remove the quotation
marks, the result should become correct:

```Python
mass = 35
double_mass = mass*2
print(f"Two times {mass} kg makes {double_mass} kg.")
```

In a the next lessons, we will look more closely at how operators (like
multiplication) work on different data types. For the moment, you can conclude
that in order to do maths with a variable, it should be a number.
</details>




## Summary 

- A variable is a named place that contains a value.
- The most common values are a number (`int`, `float`), a word (`str`), or a `True/False` statement (`bool`).
- When naming a variable, make sure that the name is short, descriptive, and consistent.
- To make a string out of several data types, you can use an f-string, like this: `output = f"The charge is {charge}"`.

