# Introduction to Python


## Overview
Python is a high-level, interpreted, interactive and object-oriented scripting language. It's one of the most popular programming languages in the world, and it's designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages. It was created in 1991 by Guido van Rossum. 

### Why Python?
- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-orientated way or a functional way.

Note: This tutorial is for Python 2. Python 3 varies from Python 2 in many ways.


## Set Up Your Programming Environment

### 1. Find out if Python is already installed on your computer.
If you're running Linux, Python is probably already installed on your system. To find out if it is installed, open a terminal and type the word **python** or **python --version**. You'll probably see output that looks something like this:
```
$ python --version
Python 2.7.15
```

### 2. Install Python, if it is **not** already installed.
Open a terminal nad run the following commands:
```
$ sudo apt update
$ sudo apt install python-pip
$ pip --version
```
[reference](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)  
[another reference](https://www.quora.com/How-can-I-install-Python-on-Ubuntu)

### 3. Install a text editor that will make it easy to run your first programs.
Geany is a simple text editor, which makes it easy to run Python programs. Output is displayed in a separate terminal window, which gets you used to working in terminals as well.
- Open a terminal, and install the package 'geany':
    ```
    $ sudo apt-get install geany
    ```
- Press the windows button, and type 'geany'
- Drag the geany icon to the task bar on the left side of the screen. This creates a shortcut you can use to start geany.


## Run Your First Python Program
- Open Geany (or any text editor you like)
- Write a [Hello World](http://introtopython.org/hello_world.html) program, and save it as 'hello.py'  
    In the .py file simply type:
    ```
    print "Hello Python world!"
    ```
    Note: the above script is for Python 2, in Python 3 this whould be:
    ```
    print('Hello Python world!')
    ```
- Run the Python program you just wrote in Geany by pressing 'F5' on the keyboard (or Build > Execute)


## Python Basics

### Python Source Code
    Python source files use the ".py" extension and are called "modules". A Python module can be run directly, or it can be imported and used by some other module. When a Python file is run directly, the special variable `__name__` is set to `'__main__'`. Therefore, it's common to have the boilerplate if `__name__ ==...` shown above to call a main() function when the module is run directly, but not when the module is imported by some other module.

### A Simple Python Program 'hello.py'
```
#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    print 'Hello there'

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
```

Program explained:
- `#!/usr/bin/env python` at the beginning of the file indicates that it's a Python program.
- `import sys` imports the sys module, which is a python script named 'sys.py'
- `def main(): ...` is a user-defined function.
- `if __name__ == '__main__': ...` executes when the module is run directly. In this example, it calls the `main()` function.
- Any line that starts with `#` is a comment and would not be executed.

### User-defined Functions
The **def** keyword defines the function with its parameters within parentheses and its code indented. The first line of a function can be a documentation string ("docstring") that describes what the function does. The docstring can be a single line, or a multi-line description. Variables defined in the function are local to that function. The return statement (if there is one) can take an argument, in which case that is the value returned to the caller.

### Indentation
One unusual Python feature is that the whitespace indentation of a piece of code affects its meaning. A logical block of statements such as the ones that make up a function should all have the same indentation, set in from the indentation of their parent function or "if" or whatever. If one of the lines in a group has a different indentation, it is flagged as a syntax error.  
A common question beginners ask is, "How many spaces should I indent?" According to [the official Python style guide (PEP 8)](http://python.org/dev/peps/pep-0008/#indentation), you should indent with 4 spaces.

### Variables, Types and Logic Statements
```
def python_basics():

    # This function contains basic python syntax and statements 
    # for beginners to refer to.

    # Below is a print command, it prints whatever string after 
    # the 'print' keyword.
    print "Hello, World!"
    # Anything behind '# ' is a comment and will be ignored at runtime.
    # --------------------------------------
    # Defining a boolean, which can only be either 'True' or 'False'
    boolean = True
    # Below is an if statement
    if boolean: # If the condition is True, do the following
        print "True"
    else:   # Otherwise, do the following
        print "False"
    # --------------------------------------
    # Defining a variable or list
    var = 0
    lst = [1, 2, 3, 4]
    # --------------------------------------
    i = 0
    # Below is a typical while loop
    while i < 10:   # while condition is True, do the following
        if i == 3:
            i += 1
            continue    # skip the rest of the commands in this 
                        # iteration and start the next iteration 
                        # immediately.
        if i == 5:
            break   # Exit the while loop immediately.
        print i
        i += 1  # i = i + 1
    else:   # Otherwise, do the following
        print "While loop ended."
```


## What's Next?
Congratulates! Now that you know the Python basics, go add your own functions and make the robot roll!


## Good To Know (optional)

### Code Checked at Runtime
Python does very little checking at compile time, deferring almost all type, name, etc. checks on each line until that line runs. Suppose you defined a **repeat()** function but not **repeeeet()**, and the above **main()** calls **repeat()** like this:
```
def main():
    if name == 'Guido':
        print repeeeet(name) + '!!!'
    else:
        print repeat(name)
```
The if-statement contains an obvious error, where the repeat() function is accidentally typed in as repeeeet(). The funny thing in Python ... this code compiles and runs fine so long as the name at runtime is not 'Guido'. Only when a run actually tries to execute the repeeeet() will it notice that there is no such function and raise an error. This just means that when you first run a Python program, some of the first errors you see will be simple typos like this. This is one area where languages with a more verbose type system, like Java, have an advantage ... they can catch such errors at compile time (but of course you have to maintain all that type information ... it's a tradeoff).

### Variable Names
Since Python variables don't have any type spelled out in the source code, it's extra helpful to give meaningful names to your variables to remind yourself of what's going on. So use "name" if it's a single name, and "names" if it's a list of names, and "tuples" if it's a list of tuples. Many basic Python errors result from forgetting what type of value is in each variable, so use your variable names (all you have really) to help keep things straight.  
As far as actual naming goes, some languages prefer underscored_parts for variable names made up of "more than one word," but other languages prefer camelCasing. In general, Python [prefers](http://python.org/dev/peps/pep-0008/#function-names) the underscore method but guides developers to defer to camelCasing if integrating into existing Python code that already uses that style. Readability counts. Read more in the section on [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions) in PEP 8.  
As you can guess, keywords like 'print' and 'while' cannot be used as variable names — you'll get a syntax error if you do. However, be careful not to use [built-ins](https://www.programiz.com/python-programming/methods/built-in/str) as variable names. For example, while 'str' and 'list' may seem like good names, you'd be overriding those system variables. Built-ins are not keywords and thus, are susceptible to inadvertent use by new Python developers. Check all built-ins [here](https://www.programiz.com/python-programming/methods/built-in/str).


## Reference
- [Google's Python Class](https://developers.google.com/edu/python/)
- [python.org](https://docs.python.org/2/)
- [tutorialspoint.com](https://www.tutorialspoint.com/python/python_basic_syntax.htm)
- [w3schools.com](https://www.w3schools.com/python/python_getstarted.asp)
- [introtopython.org](http://introtopython.org)

---

## Copyright
All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without prior written permission from Popular Robotics, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, contact Popular Robotics directly.

---

Edited by Lyuzhou Zhuang on 12/3/2018