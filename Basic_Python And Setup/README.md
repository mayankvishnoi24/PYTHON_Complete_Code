## What is Python

**
Python is a high-level, general-purpose, interpreted programming language.

1) High-level
Python is a high-level programming language that makes it easy to learn. Python doesn’t require you to understand the details of the computer in order to develop programs efficiently.

2) General-purpose
Python is a general-purpose language. It means that you can use Python in various domains including:

        * Web applications
        * Big data applications
        * Testing
        * Automation
        * Data science, machine learning, and AI
        * Desktop software
        * Mobile apps

The targeted language like SQL which can be used for querying data from relational databases.

3) Interpreted
Python is an interpreted language. To develop a Python program, you write Python code into a file called source code.
**

## Install Python

**Install Python on Windows
First, download the latest version of Python from the download page.

Second, double-click the installer file to launch the setup wizard.

In the setup window, you need to check the Add Python 3.8 to PATH and click Install Now to begin the installation.


It’ll take a few minutes to complete the setup.


Once the setup completes, you’ll see the following window:


Verify the installation
To verify the installation, you open the Run window and type cmd and press Enter:


In the Command Prompt, type python command as follows:


If you see the output like the above screenshot, you’ve successfully installed Python on your computer.

To exit the program, you type Ctrl-Z and press Enter.

If you see the following output from the Command Prompt after typing the python command:

'python' is not recognized as an internal or external command,
operable program or batch file.
Code language: Shell Session (shell)
Likely, you didn’t check the Add Python 3.8 to PATH checkbox when you install Python.

Install Python on macOS
It’s recommended to install Python on macOS using an official installer. Here are the steps:

First, download a Python release for macOS.
Second, run the installer by double-clicking the installer file.
Third, follow the instruction on the screen and click the Next button until the installer completes.
Install Python on Linux
Before installing Python 3 on your Linux distribution, you check whether Python 3 was already installed by running the following command from the terminal:

python3 --version
If you see a response with the version of Python, then your computer already has Python 3 installed. Otherwise, you can install Python 3 using a package management system.

For example, you can install Python 3.10 on Ubuntu using apt:

sudo apt install python3.10
Code language: CSS (css)
To install the newer version, you replace 3.10 with that version.

In this tutorial, you learned how to install Python 3 successfully on your computer.**

## Setup Visual Studio Code for Python

**Setting up Visual Studio Code
To set up the VS Code, you follow these steps:

First, navigate to the VS Code official website and download the VS code based on your platform (Windows, macOS, or Linux).

Second, launch the setup wizard and follow the steps.

Once the installation is completed, you can launch the VS code application:


Install Python Extension
To make the VS Code work with Python, you need to install the Python extension from the Visual Studio Marketplace.

The following picture illustrates the steps:


First, click the Extensions tab.
Second, type the python keyword on the search input.
Third, click the Python extension. It’ll show detailed information on the right pane.
Finally, click the Install button to install the Python extension.
Now, you’re ready to develop the first program in Python.**

## Python Hello World

**
Creating a new Python project
First, create a new directory called helloworld anywhere in your system e.g., C:\ drive.

Second, launch the VS code and open the helloworld directory.

Third, create a new app.py file, enter the following code, and save it:

print('Hello, World!')
Code language: Python (python)
The print() is a built-in function that displays a message on the screen. In this example, it’ll show the message 'Hello, Word!'.

What is a function
When you sum two numbers, that’s a function. And when you multiply two numbers, that’s also a function. In general, a function takes your inputs, applies some rules, and returns a result.

In the above example, the print() is a function. It accepts a string and shows it on the screen.

Python has many built-in functions like the print() function to use them out of the box in your program.

In addition, Python allows you to define your functions, which you’ll learn how to do it later.

Executing the Python Hello World program
To execute the app.py file, you first launch the Command Prompt on Windows or Terminal on macOS or Linux.

Then, navigate to the helloworld directory.

After that, type the following command to execute the app.py file:

python app.py
Code language: Python (python)
If you use macOS or Linux, you use python3 command instead:

python3 app.py
Code language: CSS (css)
If everything is fine, you’ll see the following message on the screen:

Hello, World!
Code language: Python (python)
If you use VS Code, you can also launch the Terminal within the VS code by:

Accessing the menu Terminal > New Terminal
Or using the keyboard shortcut Ctrl+Shift+`.
Typically, the backtick key (`) located under the Esc key on the keyboard.

Python IDLE
Python IDLE is the Python Integration Development  Environment (IDE) that comes with the Python distribution by default.

The Python IDLE is also known as an interactive interpreter. It has many features such as:

Code editing with syntax highlighting
Smart indenting
And auto-completion
In short, the Python IDLE helps you experiment with Python quickly in a trial-and-error manner.

The following shows you step by step how to launch the Python IDLE and use it to execute the Python code:

First, launch the Python IDLE program:


A new Python Shell window will display as follows:


Now, you can enter the Python code after the cursor >>> and press Enter to execute it.

For example, you can type the code print('Hello, World!') and press Enter, you’ll see the message Hello, World! immediately on the screen:

Python Hello World - Executing code
Summary
Use the python app.py command from the Command Prompt on Windows or Terminal on macOS or Linux to execute the app.py file.
Use the print() function to show a message on the screen.
Use the Python IDLE to type Python code and execute it immediately.
**