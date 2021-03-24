'''
# IPython - Interactive Python used for analytical computing
# Jupyter Notebooks are web version of IPython for better data visualization
# to launch "ipython" in cmd
# to launch "jupyter notebook" in cmd
# ipynb - interactive python notebook
# %<commands> are magic methods and can be executed in ipython

magic methods -
Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
The __init__ method for initialization is invoked without any call, when an instance of a class is created, like constructors in certain other programming languages such as C++, Java, C#, PHP etc. These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.


magic commands (command line programs) - IPython’s special commands (which are not built into Python itself) are known as “magic” commands. These are designed to facilitate common tasks and enable you to easily control the behavior of the IPython system. A magic command is any command prefixed by the percent symbol %.
# %run <file_name>.py <cmd-line args if any> will run the file
# Should you wish to give a script access to variables already defined in the interactive IPython namespace, use %run -i instead of plain %run.
# %load <filename>.py magic function, which imports a script into a code cell
# %paste takes whatever text is in the clipboard and executes it as a single block in the shell
# %cpaste is similar, except that it gives you a special prompt for pasting code

Frequently used magic commands
Command     Description
%quickref   Display the IPython Quick Reference Card
%magic      Display detailed documentation for all of the available magic commands
%debug      Enter the interactive debugger at the bottom of the last exception traceback
%hist       Print command input (and optionally output) history
%pdb        Automatically enter debugger after any exception
%paste      Execute preformatted Python code from clipboard
%cpaste     Open a special prompt for manually pasting Python code to be executed
%reset      Delete all variables/names defined in interactive namespace
%page       OBJECT Pretty-print the object and display it through a pager
%run scr.py Run a Python script inside IPython
%prun stmt  Execute statement with cProfile and report the profiler output
%time stmt  Report the execution time of a single statement
%timeit stmt    Run a statement multiple times to compute an ensemble average execution time; useful for
                timing code with very short execution time
%who, %who_ls, %whos     Display variables defined in interactive namespace, with varying levels of information/verbosity
%xdel variable          Delete a variable and attempt to clear any references to the object in the IPython internals



# Magic functions can be used by default without the percent sign, as long as no variable is defined with the same name as the magic function in question. This feature is called automagic and can be enabled or disabled with %automagic.


Introspection - 
Using a question mark (?) before or after a variable will display some general information about the object, or function docstring (we can write funtion docstring in """docstring here""")
(??) will give source code.
A number of characters combined with the wildcard (*) will show all names matching the wildcard expression


# None is not only a reserved keyword but also a unique instance

Datetime format specification (ISO C89 compatible)
Type    Description
%Y      Four-digit year
%y      Two-digit year
%m      Two-digit month [01, 12]
%d      Two-digit day [01, 31]
%H      Hour (24-hour clock) [00, 23]
%I      Hour (12-hour clock) [01, 12]
%M      Two-digit minute [00, 59]
%S      Second [00, 61] (seconds 60, 61 account for leap seconds)
%w      Weekday as integer [0 (Sunday), 6]
%U      Week number of the year [00, 53]; Sunday is considered the first day of the week, and days
        before the first Sunday of the year are “week 0”
%W      Week number of the year [00, 53]; Monday is considered the first day of the week, and days
        before the first Monday of the year are “week 0”
%z      UTC time zone offset as +HHMM or -HHMM; empty if time zone naive
%F      Shortcut for %Y-%m-%d (e.g., 2012-4-18)
%D      Shortcut for %m/%d/%y (e.g., 04/18/12)
'''