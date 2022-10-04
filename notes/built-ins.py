# ~~~~~~ Built-in Functions ~~~~~~ #

# Python has many built-in functions to make your life as a developer easier
# The two that we will be looking at today are print() and input()

# print() acts just as it sounds, it will take whatever is inside its parenthesis and print it to the console!

print(4)  # Will print the integer 4 (more on data types later) to the console

x = "foo"
print(x)  # Will print the string 'foo' to the console
print()  # Add some white space between our print statements

# The second built-in function that is important to us is the input() function
# input() will prompt a user from the console for an input that we can use in our code!
# Whatever is inside the input() parenthesis will be prompted to the user before asking for an input

y = input(
    "What is your name?"
)  # Console will prompt user for their name, will print "What is your name?" beforehand

# We can save the value that the user gives us into a variable and then run code around that new piece of data!

print("Your name is:", y)  # Will print whatever the user had input into the console
print()  # Add some white space between our print statements

# "But Mason, the input is on the same console line that is prompting the user and that looks kind of weird,
# can we fix that?"
# Is what you may be asking yourself... Of course we can!

# Two ways: we can use an Escape Character, or we can print our prompt before asking for an input!

# Example One: Escape Character "\n"
# Using a backslash \ indicates an escape character, there are many types of escape characters

z = input(
    "What is your name? (new line escape character)\n"
)  # \n is the escape character for "new line", the user will input their name on a new line
print("(escape character) Your name is:", z)
print()  # Add some white space between our print statements

# Example Two: Print the prompt before asking for input

print("What is your name? (printing prompt before asking for input)")
alpha = input()
print("(Print prompt before) Your name is:", alpha)
print()  # Add some white space between our print statements
