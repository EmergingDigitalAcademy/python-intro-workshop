# ~~~~~~ Conditionals ~~~~~~ #

# Sometimes we need to have the code we write make decisions, and we do that through conditional statements
# A conditional statement will take a truth or a false boolean value and a decide to run a block of
# code or not

# The conditional statements that we can use in Python are if (if something IS true do this), else (if
# something is NOT true do this instead), and elif (if the first thing was NOT true, but the second thing
# we are checking IS true, do this)

# The code that we want to be executed by our conditional needs to be in a different code block, or scope,
# than the rest of the code that we are trying to run. Most languages will differentiate code blocks by using
# some character, for example a new code block after an if statement in JavaScript is defined by using
# curly brackets ( {} ).

# In Python, however, code blocks are defined by indentation. That means that you have
# to add spaces or tabs in the line after your statement to indicate a new code block, and every line of
# code that is supposed to be grouped in a code block has to have the same indentation or you will recieve
# an indentation error.

# Examples of conditionals:

print()
print("~~~~ Conditional 1 ~~~~")
print()

temp1 = 70

# It's like asking our code, "Is the temperature high enough to wear summer clothes?"

if temp1 >= 65:
    print("The temperature is " + str(temp1) + " degrees, higher than 65.")
    print("Wear summer clothes!")

print()
print("~~~~ Conditional 2 ~~~~")
print()

temp2 = 30

if temp2 >= 65:
    print("The temperature is " + str(temp2) + " degrees, higher than 65.")
    print("Wear summer clothes!")
else:
    print("The temperature is " + str(temp2) + " degrees, lower than 65.")
    print("Wear winter clothes!")

# In this example, our code is telling us to wear winter clothes at any time the temperature is less than
# 65 degrees, but realistically I wouldn't start bundling up until about 40 degrees. We can achieve this
# logic by using an elif statement

print()
print("~~~~ Conditional 3: ~~~~")
print()

temp3 = 45

if temp3 >= 65:
    print("The temperature is " + str(temp3) + " degrees, higher than 65.")
    print("Wear summer clothes!")
    print()
elif temp3 > 40:
    print(
        "The temperature is "
        + str(temp3)
        + " degrees, lower than 65 but higher than 40."
    )
    print("Dress a bit warmer!")
    print()
else:
    print("The temperature is " + str(temp3) + " degrees, lower than 40.")
    print("Wear winter clothes!")
    print()
