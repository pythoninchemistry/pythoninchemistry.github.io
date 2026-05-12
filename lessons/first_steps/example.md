# Example

In this lesson, we will illustrate the capabilities of Python by running and
editing pre-existing code.

This program:
1. Opens a `.csv` file containing UV-Vis absorption data
2. Converts its wavelength units to energy units
3. Finds all peaks in the data above a threshold
4. Plots the spectrum and peaks to a scientific standard
5. Saves the figure as a `.pdf`

## Preparing your folder

The easiest way to allow Python programs to interact with files is to store the
source code in the same folder as the file. In this case, we need our `.py` file
and `.csv` files in the same place.

```{admonition} Task
Make a new folder for this lesson. Download this file: [benzene_uv-vis_nm.csv](benzene_uv-vis_nm.csv) (data from @RomandVodar1951). Save it in the folder, ensure the file is named `benzene_uv-vis_nm.csv` and open it in a spreadsheet editor (e.g. Excel).

Also open the file in Spyder and compare it in both programs.
```

```{tip}
Comma Separated Value (`.csv`) files are often opened as spreadsheets, which
disguises the fact that they are plain text files which can be opened in Spyder,
Notepad, TextEdit, or any other such editor. Fragments of text represent values,
where lines of text correspond to rows on a spreadsheet and commas mark the
beginning of a new column.

Formatted text, or binary files, carry more information than only textual, like
typeface, images, or computer programs. This added complexity makes them harder
to use in programming.

If you are preparing a file to be read by Python, prefer plain text files and
avoid formatted ones, like `.docx` or `.xlsx`.
```

## Syntax

What now follows is a program which reads all the lines of this file which start
with a number (allowing us to skip the header). The data is stored by the
program and the last x and y data points are printed out as a health check.

```Python
"""
UV spectrum analyser

Input a spectrum in nm units and csv format.

"""

import matplotlib.pyplot as plt

# parse csv data
file_name = "benzene_uv-vis_nm.csv"

wavelengths = []
absorbances = []

with open(file_name) as spec_file:
    for line in spec_file:
        # only conserve lines that start with a number
        # to skip header
        if line[0].isdigit():
            split_line = line.split(",")
            wavelengths.append(float(split_line[0]))
            absorbances.append(float(split_line[1]))

print(wavelengths[-1],absorbances[-1])
```

```{admonition} Task
Paste the code above into Spyder, save it in your working folder, and run it. Check that the output matches the
bottom line of your csv file.
```

Let's look at a few features of how Python is written, using this as an example.

- **Top to bottom**: Python code is made up of commands for the computer to
  follow. By default, they are ordered from top to bottom (the first line is
executed first, and so on). There are ways to override this rule for our
benefit, for example repeating a same line of code hundreds of times without needing to
write it repeatedly.

- **Indentation:** The space between the left of the screen and the beginning of
  Python code is called an *indent*. In Python, the indentation has a precise
meaning for the operation of the code, so it can't be changed freely to make the
program look neater. Generally, indentation is used to modify the top-to-bottom
operation of Python.

- **Colour:** Code editors highlight words using different colours to indicate
  their role in the Python language. It's as if in English, one colour was
reserved for verbs and another for nouns. Some words are invented by the
programmer, (like `file_name_`), but others are chosen from pre-existing words
with meaning (like `import` or `open`). Syntax highlighting allows you to notice
when you are choosing a word which is already reserved in Python.

- **Comments:** Programs can be hard to understand, even by experts. Therefore
  programmers leave explanatory text to help the reader understand what is going
on. These are called *comments*. Comments can be written by preceding them with
a hash symbol (`#`) or by encasing multiple lines by two sets of triple quotes
(`"""`).

- **Case:** Python is *case sensitive*, which means that capital and lower case
  letters are not interchangeable. Therefore, while the `print()` function is
reserved and defined in Python, `Print()` is not.

```{admonition} Task
Add a comment to the code and run it to check that it still works. Change the
capitalisation of any non-comment word, and run the code to check that you get
an error. Then return the code to its pristine state.
```

## Debugging code
Let's complete our code.


````{admonition} Task
Under your first bit of code, paste the block below, run your program, and press the "Plots" tab above the
output pane in Spyder to see the result.

```Python
# covert nm to eV
conversion_factor = 1239.84
energies = []

for wavelength in wavelengths:
    energies.append(conversion_factor/wavelength)

# find peaks
threshold = 3.0
peak_energies = []
peak_absorbances = []

# loop over each point except first and last
for i in range(len(absorbances)-4):
    # find peaks based on adjacent values
    if (absorbances[i+1] < absorbances[i+2]) and (absorbances[i+3] < absorbances[i+2]):
        # apply threshold
        if absorbances[i+2] > threshold:
            peak_absorbances.append(absorbances[i+2])
            peak_energies.append(energies[i+2])

# plot results
fig, ax = plt.subplots()
ax.plot(energies,absorbances,label="Benzene absorption",zorder=1)
ax.scatter(peak_energies,peak_absorbances,color='orange',label="Peaks",zorder=2)
ax.hlines(threshold,energies[0],energies[-1],linestyle='--',color='orange',label="Threshold")
ax.set_xlabel("Energy / eV")
ax.set_ylabel("Absorbance")
ax.legend()
plt.show()
```

Using the comments, try to understand what each section of the code
accomplishes.

````

You should see a plot on the top right of the window. The spectrum looks fine
but our peak detection seems to have failed. Our strategy was to look at each
absorbance value and check that it is strictly higher than the value before and
after.

```{admonition} Task
Investigate the `.csv` data and work out why our peak peaking strategy failed.
```

<details><summary>Solution</summary>
Due to the limited significant figures, the absorbance values at smooth peaks
are repeated in pairs, which means that neither value is strictly higher than
its neighbours.

Our solution below will compare candidate peaks with next nearest neighbours
instead.
</details>

Let's fix our code with a better peak detection strategy.

````{admonition} Task
Replace this line:
```python
    if (absorbances[i+1] < absorbances[i+2]) and (absorbances[i+3] < absorbances[i+2]):
```
with the following:
```Python
    if (absorbances[i] < absorbances[i+2]) and (absorbances[i+4] < absorbances[i+1]):
```
Taking care to include the leading spaces before `if`.

Run your code and check that more correct peaks are detected.
````
Now that our code works as intended, let's take control of it.

````{admonition} Task
Change the peak detection threshold so that you are only left with a single
detected peak.
````

<details><summary>Solution</summary>

The line to change reads:

```python

threshold = 3.0

```

Raise the value to something like:

```python

threshold = 3.7

```

</details>

## Extra functionality
We've demonstrated how to use Python in basic data processing. You can already
take this code and modify it to suit the uses of your own data.

Let's demonstrate some last tricks that are possible in Python.

````{admonition} Task

Paste the following line at the bottom of your script and run it:

```python

plt.savefig("spectrum.pdf")

```

Now search your working folder for a file called `spectrum.pdf` and open it. Try
changing the `.pdf` extension to other file types to see which ones work.

````

Finally, let's use a more complicated piece of code.

````{admonition} Task
Paste the following code at the bottom of your script and run it:

```python
import plotly.graph_objects as go

fig = go.Figure()

# plot line
fig.add_trace(go.Scatter(
    x=energies,
    y=absorbances,
    mode='lines',
    name='Benzene absorption'
))

# plot peaks
fig.add_trace(go.Scatter(
    x=peak_energies,
    y=peak_absorbances,
    mode='markers',
    marker=dict(color='orange'),
    name='Peaks'
))

# plot threshold
fig.add_shape(
    type='line',
    x0=energies[0],
    x1=energies[-1],
    y0=threshold,
    y1=threshold,
    line=dict(color='orange', dash='dash'),
)

# add labels
fig.update_layout(xaxis_title="Energy / eV",
                  yaxis_title="Absorbance",showlegend=True)

fig.show(renderer="browser")
```
Play around with this interactive visualisation of your data. You can even save
it as `.html` and put it on your own webpage!

````

## Summary

- Python can interact with files, analyse data, and plot it.
- It is executed top-to-bottom.
- Indentation is meaningful and can break the rule above.
- Syntax highlighting can help you read code.
- Comments are written with `#` or `"""`.
- Python is case-sensitive.

The next lessons will return to basics and teach you the fundamentals of Python.
By the end, you should be able to understand everything shown in this lesson's
example.
