# Opening and Using a Jupyter Notebook

## Prerequisites
- [A Python installation](/lessons/basics/write_run_python.md)

## What is a Jupyter Notebook?
Some Python code is accompanied by a mixture of text and images in what is called a workbook. This kind of code is stored in a file format called a _Jupyter Notebook_. You can recognise a Jupyter Notebook because the file name ends in `.ipynb`
.
## How to open a Jupyter Notebook
If you don't already have a Jupyter Notebook file, you can {download}`download a text file<./downloads/example_notebook.ipynb>`.

## Instructions

If you installed Python using [Anaconda](/lessons/basics/write_run_python.md#installation) then Jupyter will have already been installed. If you used a different method you might need to install it. 

If you used conda then use the following command:

```bash
conda install conda-forge::jupyter
```

if you made a basic Python install then use pip:
```bash
pip install jupyter
```

### Open JupyterLab
If using Anaconda **Search for the program _Anaconda Navigator_ and open it**. After a few seconds, you should see a window like this appear:

![Window showing six logos for different programs. A red arrow points to the "Launch" button below the top right logo.](/lessons/basics/images/navigator_jupyterlab.png)

**Press the "Launch" under JupyterLab.** 

Otherwise from a terminal type:
```bash
jupyter lab
```
This will open a tab on your default web browser which should look like this:

![Window showing a folder navigation menu on the left and a Python 3 logo on the right.](/lessons/basics/images/jupyterlab.png)

Look at the address bar at the top of your browser. It should read `localhost` followed by some numbers. This means that you are not actually accessing the internet, despite being on a web browser. The page is generated locally by your computer, so you don't need an internet connection to work on your Jupyter Notebook.

**In the sidebar on the left, search through your folders for your `.ipynb` file and double-click on it.** If you just downloaded this file, it might be in your _Downloads_ folder. Your screen should now show this:

![Screenshot of a Jupyter Notebook.](/lessons/basics/images/example_notebook.png)

You have just opened the Jupyter Notebook.

## How to use a Jupyter Notebook
Jupyter Notebooks are split into horizontal segments called _cells_. You can see which cell is selected because it has a vertical blue bar on the left of it, as you can see in the screenshot above. If you click on another part of the notebook, you will select another cell.

There are two important kinds of cells: _Markdown_ and _Code_.

You can tell what kind a cell is by looking at the top ribbon:

![Top bar of the Jupyter Notebook with the word "Markdown" circled in red.](/lessons/basics/images/top_bar.png)

### Markdown cells
Markdown cells can contain formatted text and images. To change this content, **double-click on the cell**. This will show you the unformatted text, which has been written using a language called "Markdown":

![A box of raw Markdown text.](/lessons/basics/images/raw_markdown.png)

To make the text appear formatted again, make sure that the cell is selected, and **click on the "Run" button in the top ribbon** (Shortcut: Shift + Enter):

![Top bar of the Jupyter Notebook with the "run" triangle circled in red.](/lessons/basics/images/run_button.png)

### Code cells
Code cells contain programming code; in this case—Python. **Select the code cell, and run it, just like you ran the Markdown cell.** The result should look like this:

![Code cell showing "print(753+247)", and below, the result: 1000.](/lessons/basics/images/code_cell.png)

Observe how the output of the Python code (the number 1000) is printed below the cell. Additionally, a new empty code cell was created below, to let you continue writing code.

## Advice
Jupyter Notebooks are very good if you want someone else to use your code and your text in the same place. They also have a lot of options for being hosted online. Good uses for a Jupyter Notebook could be:
- A tutorial where you want to mix written instructions with runnable code.
- A data science report, where you generate figures along with the explanation for the origin of the data.
- A programme where you want the user to modify the source code, but they can't run Python on their own computer.

You should avoid using a notebook in these situations:
- You care about reproducibility: Notebook cells can be run in any order, and also deleted after running. All of this is information hidden from the user which could affect the results of the program.
- You are conducting a long-term project: Notebooks are not written in plain text (i.e. they don't look readable when opened in a notepad). Therefore, if you have multiple versions of one project, it's very hard to find exactly what the differences between versions are. In contrast, for plain text files, there are automatic tools for this.
- Your user doesn't need to see the source code: Notebooks always show you the original Python code which they are running. Usually, the user would prefer not to read this text before running a program because it is slow and pointless.

If you find yourself in any of these situations, you should prefer to write your code in a Python file, which is a plain text file ending in `.py`.
