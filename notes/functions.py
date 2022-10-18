# ~~~~~~ Functions ~~~~~~ #

# Functions are another way that we can organize our code so we aren't writing the same code multiple times!
# You can think of a funciton like a factory. To make a pencil, we are always feeding the same ingredients
# (wood, graphite, metal, and rubber) into a factory, and the output is always the same, we are given a pencil!

# We have actually been using many built in functions throughout the course so far. print(), str(), and
# input() are all built-in functions that Python offers us.

# To define a function we use the def keyword followed by our function name, a pair of parenthesis, and ending
# with a colon. Any code that we want our function to run needs to be in an indented code block following the
# colon.

# Similarly to any other code block that we make in Python (code run in an if statement or in a for loop),
# nested code blocks can access anything written within the global scope (anything written
# normally within the file), but anything else written outside of the scope of the code block cannot access
# variables or code written within the nested code.

# In other words, code written in a function is limited to that function.

# To execute the code written within a function, we have to call the function. That is done similarly to
# calling a variable, except we follow the call with a pair of parenthesis.

# Example of a custom function:


def customFunction():
    print()
    print("~~~~ Custom Function ~~~~")
    print()

    def greeting():
        print("What is your name?")
        name = input()
        print()
        print("Your name is " + name)
        print()

    greeting()


# We can always access variables created outside of the function in the scope of the function, but what if
# we don't know what are variables are going to be, or we want to pass data in to a function without
# declaring variables in the first place, we can use arguments.

# Arguments are like variables created for the function, but we don't define what the data in the
# argument is until we call the function

# Arguments are defined when you define your function, write the argument name in the parenthesis of the
# function definition. Each function can take multiple arguments, separate arguments in parenthesis with
# commas.

# To get data out of the function, we use the return keyword. Anything on the same line following the return
# keyword will be returned out of the function after the function is finished executing.

# Examples of Arguments and Returns:


def argumentsAndReturns():
    print()
    print("~~~~ Function Arguments and Return ~~~~")
    print()

    def sumFunction(number1, number2):
        sum = 0
        sum += number1
        sum += number2
        return sum

    return1 = sumFunction(1, 3)
    return2 = sumFunction(6, 8)
    return3 = sumFunction(2, 19)
    return4 = sumFunction(1234, 9876)

    print("sumFunction ran with numbers 1 and 3 and returned " + str(return1))
    print()
    print("sumFunction ran with numbers 6 and 8 and returned " + str(return2))
    print()
    print("sumFunction ran with numbers 2 and 19 and returned " + str(return3))
    print()
    print("sumFunction ran with numbers 1234 and 9876 and returned " + str(return4))
    print()


# So far all the code written in the notes has been written in the global scope of the files, but that is not
# the proper practice when writing code. It is common to define a "main" function in a file to run the code
# that you want to run when the file loads, or to run functions that run the the code itself.

# Just don't forget to call your main function!

# Example of a main function:


def main():
    customFunction()
    argumentsAndReturns()


main()
