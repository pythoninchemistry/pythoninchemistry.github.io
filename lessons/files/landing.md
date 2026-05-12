# Files

## Learning outcomes

*   Read the contents of a text file.
*   Write new text files.

## Prerequisites

- [First steps](/first_steps/landing.md)
- [Variables](/variables/landing.md)
- [Control flow](/control_flow/landing.md)

## Reading files
Python has functionality to read any kind of computer file. However, making sense of a text, image, or sound file represents three very different tasks. In this lesson, we will focus on text files, since their manipulation is so common in science.

There are many different file opening methods in Python, which you may encounter especially in older programmes. Here, we will only focus on the `with open()` method, which has been recommended since Python 3.

Let's try it with an example. Download this text file ([molecule_names.txt](molecule_names.txt)) and rename it as `molecule_names.txt`. Then, copy the following example and place both the Python script containing the example (ending in `.py`) and `molecule_names.txt` in the same folder.

```Python
with open("molecule_names.txt") as file_in:
    lines_in_file = file_in.readlines()

print(lines_in_file)
```

- `with open("molecule_names.txt")` indicates that we are going to read a file called `molecule_names.txt`. This name can be replaced by any other file, but it needs to be in the same folder as your Python script to run. This restriction can be avoided by replacing the file name by a computer path indicating exactly where the file is on your computer.
- `as file_in:` assigns our file to a variable in Python: `file_in`. This variable is of a new data type called `TextIOWrapper`, which we can loosely understand as referring to the opened file. If we want to read from the file or write to it from now on, we can refer to the file as `file_in` rather than by its name (which remains just a string).
- `lines_in_file = file_in.readlines()` this is a specific way of reading text from a file. The function `file_in.readlines()` returns a list of strings, one per line of the file. However we decide to manipulate `file_in`, it needs to be done within this indentation. When the indentation ends, Python closes the file. Even if this closing is implicit, it's important to operate so that a file isn't being modified by Python and another program at the same time, yielding two conflicting versions of the file.

This final line allows us to manipulate all the information from the file, however when manipulating very large data sets, we may not want to keep all of the contents of the file in Python memory. To access files only line by line, a less intuitive but more general syntax exists. Here, we iterate over the file variable using a `for` loop, which yields each line as an individual string:

```Python
with open("molecule_names.txt") as file_in:
    for line in file_in:
        print(line)

```

Try adding more molecules to `molecule_names.txt` and ensure that they are printed by the code above.

```{admonition} Task
The following file [acetone.jdx](acetone.jdx) (data from @Linstrom1997-dp) contains the IR spectrum of acetone.

Save every line of the file as a string and append it to a list, ignoring any line that starts with `#`. Then, print the first and final lines that you saved.

```

<details><summary>Solution</summary>
Experimental text files often start with information about the instrument used to record the data (so called **metadata**). In this file, those lines all start with `#`.

```Python
data_lines = []

with open("acetone.jdx") as acetone_file:
    # loop over every line
    for line in acetone_file:
        # check that the line doesn't start with #
        if line[0] != "#":
            data_lines.append(line)

print(data_lines[0])
print(data_lines[1])
```
Usually, it takes some effort to extract exactly the data that we want from a file. Here, we wanted to remove the metadata, so we added a condition based on the `#` character. This operation is prone to error, so it's good to operate a sanity check by printing the first and final line, ensuring that we didn't accidentally remove a line we cared about.
</details>

````{admonition} Task
The data in `acetone.jdx` are organised as such:
```
wavenumber transmittance_1 transmittance_2 transmittance_3 transmittance_4 transmittance_5
wavenumber transmittance_1 transmittance_2 transmittance_3 transmittance_4 transmittance_5
...
```
where the wavenumber is in inverse centimetres and the five transmittance values are dimensionless and repeat measurements at the same wavenumber.

Generate two lists of floats:
- `wavenumbers` should contain all the wavenumbers in inverse centimetres.
- `transmittances` should contain the average of the five transmittances for each wavenumber.

Then, show the results with this block of code:

```Python
import matplotlib.pyplot as plt
plt.plot(wavenumbers, transmittances)
plt.show()
```

Hint: to separate a string into a list of strings based on the position of the whitespaces, use `list_of_substrings = example_string.split()`.
````

<details><summary>Solution</summary>
This task has many possible solutions. In any case, some `for` loops will be required and the numbers read in a strings should be converted to floats.

```Python
wavenumbers = []
transmittances = []
with open("acetone.jdx") as acetone_file:
    # loop over every line
    for line in acetone_file:
        # check that the line doesn't start with #
        if line[0] != "#":
            # separate the line into substrings
            split_line = line.split()
            # the first number is a wavenumber
            wavenumbers.append(float(split_line[0]))
            # average all the other numbers
            current_transmittance = 0
            for number in split_line[1:]:
                current_transmittance = current_transmittance + float(number)
            # find the average of five measurements
            current_transmittance = current_transmittance / 5
            transmittances.append(current_transmittance)

# plot
import matplotlib.pyplot as plt
plt.plot(wavenumbers, transmittances)
plt.show()
```
</details>

## Writing files
The syntax for writing files is very similar to the one for opening them, but you should exercise extra caution:
- Writing a Python file will overwrite any pre-existing file with the same name and location.
- If you try to overwrite a file that is already open by a different program, the results may be unexpected (for example, on Windows, Python will return an error).

Here is the syntax:
```Python
with open("new_molecule_names.txt","w") as file_in:
    file_in.write("paracetamol\n")
    file_in.write("butadiene")

```
- `open("new_molecule_names.txt","w")` includes a second argument for the `open()` function: `"w"`. This stands for "writing", and indicates that a new file should be created with the desired name.
- `file_in.write("paracetamol\n")` shows how the `file_in.write()` command works. Any string that is given as an argument is added to the file. Here, the `\n` translates into a new line in the resulting file.

Check that `new_molecule_names.txt` was indeed created and contains what you expect.

````{admonition} Task
Let's say you want to share the results of your acetone analysis as a spreadsheet. Write a Python program which exports the results as a file called `acetone_ir.csv`. The first line should read `wavenumber,transmittance` and every following line should contain the a wavenumber value followed by the averaged transmittance at that wavenumber.

For example, the beginning of the file should read:
```
wavenumber,transmittance
450.0,0.9294399999999999
...
```
Open the final result in a spreadsheet editor, like Excel.
````

<details><summary>Solution</summary>
We will start identically to before.

```Python
wavenumbers = []
transmittances = []
with open("acetone.jdx") as acetone_file:
    # loop over every line
    for line in acetone_file:
        # check that the line doesn't start with #
        if line[0] != "#":
            # separate the line into substrings
            split_line = line.split()
            # the first number is a wavenumber
            wavenumbers.append(float(split_line[0]))
            # average all the other numbers
            current_transmittance = 0
            for number in split_line[1:]:
                current_transmittance = current_transmittance + float(number)
            # find the average of five measurements
            current_transmittance = current_transmittance / 5
            transmittances.append(current_transmittance)

with open("acetone_ir.csv","w") as file_in:
    # write the column headers
    file_in.write("wavenumber,transmittance\n")
    for wavenumber, transmittance in zip(wavenumbers, transmittances):
        file_in.write(f"{wavenumber},{transmittance}\n")

```
This solution is slightly computationally inefficient because we are looping through every line of the input file, and then looping over each result again to write out the result. A less legible but more efficient solution would be to nest both `with open()` blocks, so that as each line is read in the input, a new line is immediately written to the output. 
</details>

## Summary
- Before reading a file in Python, make sure it is in the same directory as your code (or has a valid filepath). 
- Open a file using `with open("file.txt") as file_in:`.
- Before writing a file, ensure that it isn't going to overwrite something important.
- Close any file likely to be overwritten.
- Use the syntax `with open("file.txt", "w") as file_in:` and then `file_in.write()` to write to the file.
- `\n` renders as a new line in the file.