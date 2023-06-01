# ~~~~~~ Functions ~~~~~~ #

# Pip is the included tool in Python that we use to manage our packages that we install.

# Pip comes standard in Python and links to the Python Packaging Index (pypi.org) to install packages to your
# projects. pypi.org is an extensive website shared by the Python community where people ship packages to for
# anyone to use.

# We are going to use pip to install the 'requests' package, so we can make HTTP requests from our scripts!

# To use pip, first make sure your virtual environment is activated (see venvs.py) and run the command:

# python3 -m pip install requests
# (just python on windows, no python3)

# If you look in our 'venv' folder, then in the lib / python3.10 / site-packages folder, you will see a new
# folder called 'requests'!

# Running the install command will install the package and any other packages that package will depend on.

# To uninstall a package, run the command:

# python3 -m pip uninstall <package_name>

# Uninstalling a package will uninstall that package, but NOT its dependencies.

# There are two more important pip commands, list and show.
# 'pip list' will list all packages that are installed in the current environment, and 'pip show' followed by the
# package name will show all the details for that package.

# To use requests in our script we can use the import keyword

# Example of importing a package to a file:

import requests
