# Using the command line

It is often necessary (or quicker) to run Python from the command line. This is a *very* quick guide to using a command line, it will get you started.

The first step is to open your terminal. How you do this depends on the type of PC you are using.

On Windows see if the following are installed:
-   Terminal (this is a more modern implementation)
-   Powershell (if you have conda installed run Anaconda Powershell Prompt)
-   Cmd (this is considered a bit out of date now, if you have conda installed run Anaconda Prompt)

On a Mac
-   Terminal

On Linux it will depend on your distro. Generally look for an app called one of the following:
-   Terminal
-   Command
-   Prompt
-   Shell

Once opened we can do various things. Initially it should look something like this:

![An image of a terminal with just the current directory showing](/lessons/solving_problems/images/term_1.png)

Depending on the 'shell' that you have you might have more information, such as your user name. We can now enter commands into this prompt.

Most useful will be 

| Command | Effect |
|---|---|
| *cd* | Followed by a path will change directory |
| *ls* | Lists the contents of the current directory |
| *mkdir* | Followed by a name will create a directory of that name |

When we type a path we can do so in two ways. Either absolute or relative. Absolute is a full path from the users *root* directory. This is normally the folder you start in when you open a terminal. In the example above we start in Users/User. Say we want to open the Documents folder that is in this User folder. We can type the following:

```bash
 cd Users/User/Documents
```
However, we can also  do a relative path.

```bash
cd ./Documents
```
Here the path is relative to which ever directory we are *currently* in. A single period means the current folder while two periods means go up a level.

For example, when we are in the Users/User/Documents folder, if we type:

```bash
cd ../
```
Then we will move back into the Users/User folder. Or again starting in Users/User/Documents
```bash
cd ../../
```
this will move us up two levels in the Users folder

To then run a Python script, easiest is to navigate to the folder where the script is and run the following (assuming that the script is call python_prog.py)

```bash
python ./python_prog.py
```

