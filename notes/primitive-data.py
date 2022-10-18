# ~~~~~~ Primitive Data Types ~~~~~~ #

# In Python, there are four different primitive data types: Integers, Floats, Strings, and
# Booleans.

# Variables: Variables are what we use to "hold" the data that we are working with! Variable
# names are mostly arbitrary, meaning that most of the time it does not matter what you name
# your variable. However, there are some rules:

# Variables must start with an alphabetical character, never a numeric character
# Variables cannot be the same name as any keywords within the programming language

# Bad variable name examples:

# 123iAmBad = "I am a bad variable name"
# if = "I am a bad variable name"

# To hold data inside of a variable, use the equals (=) operator!

# Integers: Integers are used to represent number data, more specifically, whole numbers from
# negative infinity to positive infinity

# Examples of integers:

integers = [0, 1, 2, 3, 4]

# Floats: "Float" is short for "floating point number," or numbers that end in a decimal figure

# Examples of floats:

floats = [0.5, 1.0, 3.14, 123.456789]

# Strings: Strings are a collection of characters enclosed in single quotes ('') or double quotes ("")
# Strings are the data type in Python that we use to determine a text data type

# Example of a string:

string = "I am a string!"

# There are many built in functions that we can use to modify our strings, but probably the most
# powerful is the addition operator (+) which we can use to concatonate, or combine, two strings together!

stringOne = "I am "
stringTwo = "a string!"

concatonatedString = stringOne + stringTwo

print()
print("~~~~ Concatonatted string ~~~~")
print()

print(concatonatedString)  # Will print "I am a string!"

# Booleans: Booleans can only take two values, True and False. Booleans are useful in conditional and comparison
# expressions

# Examples of booleans:

booleanTrue = True
booleanFalse = False

print()
print("~~~~ Boolean in use ~~~~")
print()

if (
    booleanTrue == True
):  # Will print "I am true!", change booleanTrue to booleanFalse to recieve different output
    print("I am true!")
else:
    print("I am false!")

# Data Type Conversions: Sometimes you will be working with data and you will find yourself needing a different
# data type than what you are given or what you are working with! Python makes this really easy for us as
# developers by giving us more built-in functions!

print()
print("~~~~ Data conversions ~~~~")
print()

# type(): the type() function will return the data type of what you provided in the parenthesis

stringToFloat = "4"
print(stringToFloat)  # Will print "4" (string)
print(type(stringToFloat))  # Will print <class 'str'>
print()

# int(): the int() function will return the data type provided, but as an integer instead!

stringToFloat = int(
    stringToFloat
)  # Setting the variable stringToFloat to the return of int(stringToFloat)
print(stringToFloat)  # Will print 4 (integer)
print(type(stringToFloat))  # Will print <class 'int'>
print()

# float: the float() function will return the data type provided, but as a float instead!

stringToFloat = float(stringToFloat)
print(stringToFloat)  # Will print 4.0 (float)
print(type(stringToFloat))  # Will print <class 'float'>
print()

# There are also str() and bool() functions that will convert data into strings and booleans, respectively.
