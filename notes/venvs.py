# ~~~~~~ Virtual Environments ~~~~~~ #

# A Virtual Environment in Python is a localized development environment specific to your project.

# Why do we need virtual environments? Well, Python is a system level language. When we install a package
# for a project, it would be installed to the system level environment that Python uses. There could be a lot
# of processes on your machine that depend on Python and for that reason, we don't want to pollute the system
# environment with packages.

# To create a virtual environment open a Command Line Interface

# (Linux / MacOS: Terminal, Windows: Command Prompt)

# and navigate to the project folder. Then run the command (without quotes)
# 'python3 -m venv venv' (just python, no 3, on windows).

# This will create a new folder in our project called 'venv' that includes all of the environment information
# that is localized to this project including installed packages and different python configurations.

# To install packages, we need to activate your virtual environment. If you look in the 'venv' folder,
# then in the 'bin' folder, you will see a file called 'activate.' If we run this file from our command line
# we will activate the virtual environment.

# To do that, run the command (without quotes):
# Linux / MacOS: '. venv/bin/activate'
# Windows: 'venv\Scripts\activate.bat'
# Windows PowerShell: 'venv\Scripts\activate.ps1'

# After running this command, you will see a (venv) in your CLI indicating that your virtual environment
# is activated.

# To deactivate a virtual environment, run the command 'deactivate'

# We can throw a flag into our Python environment that will not let us install packages unless we are in an activated
# virtual environment. I do recommend turning that flag on, to do so, run the command:

# export PIP_REQUIRE_VIRTUALENV=true
