# Lists and dictionaries
## Learning outcomes

*   Create and modify lists and dictionaries
*   Extract information from them

## Prerequisites

- [First steps](/first_steps/landing.md)
- [Data types](/variables/data_types.md)

## List
### Writing lists

A list (`list`) is a collection of any number of values. To declare a list, write different values in between square brackets `[]` and separated by commas.

```python
elements = ['H', 'He', 'Li']
print(elements)
print(type(elements))
```

Lists can contain more lists. A list containing lists (which themselves could contain more lists) is called a _nested list_. To make them more legible, we often write them over several lines.

```python
# A list of molecules where each molecule is represented by a list of atoms
molecules = [["H","H","O"],["H","H","H","H","C"]]

# The list can identically be written like this
molecules = [["H","H","O"],     # water
             ["H","H","H","H","C"]] # methane

print(molecules)
```

````{admonition} Task
Writing lists of lists requires a lot of brackets, which can lead to typos. What follows is a broken list which should contain two lists: the first with the numbers 0.1, 0.2, and 0.3, and the second with 1.0, 2.0, and 3.0. Find the errors in this list and fix them:

```Python
coordinates = [[0.1, 0.2, 0.3[]1.0, 2.0 3.0]]
print(coordinates)
````

<details> <summary>Solution</summary>

You should keep close track of both the commas inside each sublist and in between each sublist:
```Python
coordinates = [[0.1, 0.2, 0.3],[1.0, 2.0, 3.0]]
print(coordinates)
```
</details>

### Appending
Once created, a list can still be modified. If we want to make a list longer, we can use the `.append()` function, to add elements at the end of the list. Be careful, the syntax for `.append()` is different from what we have seen so far:
```Python
elements = ["H", "He"]
elements.append("Li")
print(elements)
```
This may be longer than just writing `["H", "He", "Li"]`, but will come in handy when we want to make very long lists. We will be able to ask Python to run the appending line multiple times, instead of manually writing a never-ending list.

Note how we named the list we wanted to lengthen (`elements`), added a full stop (`.`), called the `append()` function, and gave it, as an argument, the value we wanted to append to our list (`"Li"`). This is a typical syntax for built-in functions which are unique to a data type (technically called *methods*). Here, appending has a meaning for any list, but not for any other data type.

````{tip}
Another useful method which will come in handy when reading data from files is `.split()`. This is a method for strings which makes a list out of a string based on a given separator which divides the list. As an example, try the following piece of code and check that you understand what role the comma plays:
```Python
molecules = "carbon dioxide,ammonia,oxygen"
print(molecules.split(","))
```
````

### Length of a list
We sometimes may be called to find out the length of a list. The built-in function `len()` gives us an easy solution:
```Python
molecules = ["carbon dioxide", "ammonia", "oxygen"]
print(len(molecules))
```
Try adding molecules and verify that the output changes as you expect.

## Dictionaries

A dictionary (`dict`) also contains multiple values, like a list. However, a dictionary always contains entries in the form of pairs. The first part of the pair is called the "key", and represents the known value (like a word in a real dictionary). The second part is the "value" and represents the unknown value (like the definition). To declare a dictionary, write pairs of "keys" and "values" in between curly braces `{}` like this: `{key_1: value_1, key_2: value_2}`.

```Python
atomic_weights = {
  "Hydrogen": 1.008,
  "Helium": 4.002602,
  "Lithium": 6.941
}

print(atomic_weights)
print(type(atomic_weights))
```

```{admonition} Task
The pK<sub>a</sub> of methanol is 15.3. For ammonia, it's 32.5. Write a dictionary where the names of these molecules are the keys, and the values are their pK<sub>a</sub>s.
```


<details> <summary>Solution</summary>

Here is the correct syntax. Make sure that your colons `:` and commas `,` are in the right places!

```Python
pKas = {
'methanol' : 15.3,
'ammonia' : 32.5,
}
```
</details>

````{admonition} Task
Can you work out what information is contained in `data`?
```Python
data = {
'H' : [[1.007825, 99.9885],[2.014102, 0.0115]],
'C' : [[12.0, 98.93],[13.003355, 1.07]],
'N' : [[14.003074, 99.632],[15.000109, 0.368]],
'O' : [[15.994915 , 99.757],[16.999132, 0.038],[17.999160,0.205]]
}
```
````
<details> <summary>Solution</summary>
Here, we can clearly see why descriptive variable names could be useful. The word `data` is not helping us at all.

In fact, this is a dictionary containing lists of lists of two numbers. The keys are clearly element symbols. As for the values, if we look at each pair of numbers carefully, the first is always close to an integer, much like an atomic mass, and the second is always just under 100 or just above 0.

With these clues, we could guess that this dictionary contains a list of the atomic masses and abundances of different isotopes for each of four elements.
</details>

## Accessing parts of a list or dictionary
### Indexing lists

It can be handy to store sequences of data into a list. For example, if we want to store an absorption spectrum of 100 data points, we just need one list for absorbance and another for wavelength, instead of 200 variables containing different floats.

However, we can find ourselves wanting to access only one part of the list at a time. To this end, we can use _indexing_. To indicate that we are only referring to a specific element of a list, we follow the name of the list by a number in square brackets:

```python
elements = ['H', 'He', 'Li']
print(elements[1])
```

In this example, we used the number `1`, which returned the _second_ element of the list. This is because the Python programming language counts the position of an element in a list starting from `0`. This position is called the _index_.

````{admonition} Task
Print the first element of this list:

```Python
elements = ['H', 'He', 'Li']
```
````

<details> <summary>Solution</summary>
All you have to do is to use the index `0`.

```Python
elements = ['H', 'He', 'Li']
print(elements[0])
```
</details>

If you want to count indices from the end instead of the beginning, use negative numbers and start from `-1`:
```python
elements = ['H', 'He', 'Li']
print(elements[-1])
```

### Slicing
You may also need to access ranges of values within a list. In this case, instead of writing one index, write two of them separated by a colon `:`. The resulting list will be the range of values between the two numbers, including the first value and excluding the last. This process is called _slicing_.

```python
elements = ['H', 'He', 'Li', 'Be']
print(elements[1:3])
```

Note how `Be` was not printed, despite the fact that it corresponds to `elements[3]`.

````{admonition} Task
Indexing and slicing gets a little more delicate when dealing with nested lists. Try to extract the list `[2,3]` from the following nested list:

```Python
elements = [[1,2,3,4],
            [5,6,7,8]]
```
````

<details> <summary>Solution</summary>
It may help to work step by step. First, we want to isolate the first sublist (`[1,2,3,4]`). Since it's the first list, we can use the index `0`:

```Python
elements = [[1,2,3,4],
            [5,6,7,8]]
print(elements[0])
```

Thanks to this, we can verify that `elements[0]` indeed corresponds to the first sublist, so we can further slice this list by adding more square brackets:

```Python
elements = [[1,2,3,4],
            [5,6,7,8]]
print(elements[0][1:3])
```
</details>

````{admonition} Task
Print the list containing `Li` and `Be` by slicing the following list:

```Python
elements = ['H', 'He', 'Li', 'Be']
```
````

<details> <summary>Solution</summary>
We should change the indices accordingly.

```Python
elements = ['H', 'He', 'Li', 'Be']
print(elements[2:4])
```
</details>

### Accessing dictionary values
You can also use access values inside dictionaries but the syntax is different than for lists. Here, instead of writing a number in square brackets, you write a key. In return, you will obtain the corresponding value:

```python
atomic_weights = {
  "Hydrogen": 1.008,
  "Helium": 4.002602,
  "Lithium": 6.941
}

print(atomic_weights["Helium"])
print(type(atomic_weights))
```

````{admonition} Task
Print the atomic weight of lithium, using the dictionary provided:

```Python
atomic_weights = {
  "Hydrogen": 1.008,
  "Helium": 4.002602,
  "Lithium": 6.941
}
```
````

<details> <summary>Solution</summary>
Simply use `"Lithium"` as the key:
```Python
atomic_weights = {
  "Hydrogen": 1.008,
  "Helium": 4.002602,
  "Lithium": 6.941
}
print(atomic_weights["Lithium"])
```
</details>

## Summary 

- Lists can store multiple values in one same variable. They use `[]`.
- Dictionaries can do this too but are only useful when we will later want to access values by using keys. They use `{}`.
- You can use indexing or slicing by writing the name of a list followed by square brackets containing numbers: `masses[3:5]`.
- For a dictionary, instead of numbers, write the key inside the square brackets: `masses['Li']`.