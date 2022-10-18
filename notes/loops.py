# ~~~~~~ Loops ~~~~~~ #

# In previous examples throughout the notes, you may have noticed that I was repeating the same lines of code
# a lot. This can get redundant, and can cause our programs to be unnecessarily long. How do we solve the
# problem of running the same code multiple times? Loops!

# The most basic loop would be a for in loop. We can use the for and in keywords to loop over a list of items
# and perform repeated code to every item in the list!

# Example of a for in loop:

sum = 0.00
expenses = [10.00, 7.54, 8.32, 11.46, 15.99]

print()
print("~~~~ Basic For In Loop ~~~~")
print()

print("The current sum is " + str(sum))
print()

for expense in expenses:
    sum += expense

    print("I am the variable 'expense' in the for in loop, my value is " + str(expense))
    print("The new sum is " + str(sum))
    print()

# Say we wanted to make a loop to run some code, but we didn't have a list to loop over. There are two ways we
# can solve this problem: or we can use a range() function, or we can use a new loop keyword, while!

# The range() function will generate a range for us that we can then use a for in loop to loop over.
# The range() function takes two arguments inside of the perenthesis, a starting point and an ending point.
# The range will always end one number BEFORE the number you specify as your end point, and if you don't
# specify a start point, your start poing will be 0

# If you called range(6), you would get a range of numbers

# Example of range():


print()
print("~~~~ Range Loop ~~~~")
print()

for x in range(5):
    print("I am the variable 'x' in the range loop, my value is " + str(x))
    print()

# Think of the while keyword as catch, we want to run a loop a certain amount of times WHILE
# some condition is true

# Example of while:

i = 0

print()
print("~~~~ While Loop ~~~~")
print()

while i < 5:
    print("I am 'i', short for index, and my value is " + str(i))
    print("My loop will stop when my value is less than 5")
    print()

    i += 1

# There are a few extra keywords that we can use to make our loops more interesting: else, break, and continue.

# Else in a loop works similarly to how else works in a conditional, it will run any code in the else block
# after every itteration of the loop cycle completes.

# Example of Else:

print()
print("~~~~ For In loop with Else ~~~~")
print()

for x in range(5):
    print("I will run the code in the else block in " + str(5 - x) + " iterations.")
    print()
else:
    print("I am from the else block!")
    print()

# Break and Continue will work similarly to each other. you can use the break keyword to break out of a loop
# if some condition is matched, and you can use the continue keyword to skip a loop iteration if some
# condition is matched

# Example of Break and Continue:

print()
print("~~~~ Break keyword ~~~~")
print()

for x in range(5):
    print("I am x, my value is " + str(x))
    if x == 2:
        break
    else:
        print(
            "I am from the loop using the break keyword, I will stop iterating when x = 2"
        )
        print()

print()
print("~~~~ Continue keyword ~~~~")
print()

for x in range(5):
    print("I am x, my value is " + str(x))
    if x == 2:
        print()
        continue
    else:
        print(
            "I am from the loop using the continue keyword, I will skip the iteration when x = 2 and continue again"
        )
        print()
