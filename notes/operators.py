# ~~~~~~ Operators ~~~~~~ #

# What are operators? Operators are characters in Python that are used to perform operations on
# values and variables!

# Operators are broken up into many different categories, today we will be talking about; Arithmetic,
# Assignment, Comparative, Logical, and Memory / Identity operators.

# Arithmetic Operators: There are seven different arithmetic operators; the addition (+), subtraction (-),
# multiplication (*), division (/), modulus (%), exponential (**), and the division floor (//) operator.

# The first four and the exponential arithmetic operators are pretty standard, they all function as their name
# suggests. The modulus operator is used to find the remainder of a division operation, and the division
# floor operator is used to return an integer after a division operation whereas the base division operator
# will return a float after a division operation.

# Examples of Arithmetic Operators:

print()
print("~~~~ Arithmetic Operators ~~~~")
print()

print(4 + 4)  # Will print 8 (int)
print(10 - 2.0)  # Will print 8.0 (float)
print(3 * 6)  # Will print 18 (int)
print(100 / 8)  # Will print 12.5 (float)
print(100 // 8)  # Will print 12 (int)
print(3**3)  # Will print 27 (int)
print(15 % 7)  # Will print 1 (int)

# Assignment Operators: Assignment operators are used to assign values to variables. We have already worked
# with one and the most basic assignment operator, just the base equals (=).

# The other assignment operators come in when we want to do arithmetic and assign the result to a variable at
# the same time! There is an assignment operator to pair with all of the arithmetic operators listed above;
# +=, -=, *=, /=, %=, **=, and //=. For context, if you had a variable named sum, and you were using it to
# hold a running sum of a list of numbers, you would have to call sum in the arithmetic operation if we weren't
# using a special assignment operator.

# Examples of Assignment Operators:

print()
print("~~~~ Assignment Operators ~~~~")
print()

sum = 0
sum = sum + 2
print(sum)  # Will print 2

# We can simplify that expression down using the special assignment operator, +=

sum += 2
print(sum)  # Will print 4

# Comparative Operators: Comparative operators are used to compare to two values or variables. The result
# of a comparative operation will either be a True or False Boolean value. The comparative operators
# available in Python are; equal (== is x equal to y), not equal (!= is x not equal to y),
# greater than (> is x greater than y), less than (< is x less than y), greater than or equal to (>=),
# and less than or equal to (<=).

# Examples of Comparative Operators:

print()
print("~~~~ Comparative Operators ~~~~")
print()

x = 1
y = 2

print(x == y)  # Will print False
print(x != y)  # Will print True
print(x > y)  # Will print False
print(x < y)  # Will print True
print(x >= y)  # Will print False
print(x <= y)  # Will print True

# Logical Operators: Logical operators are used to combine conditional and comparative statements. Like
# the comparative operators, the result of a logical operation will be a True or a False Boolean value.
# There are three comparative operators; and (will return True if BOTH statements are true), or (will return
# True if EITHER statements are true), and not (will reverse the result of a logical operation, returns
# False if the result is True).

# Examples of Logical Operators:

print()
print("~~~~ Logical Operators ~~~~")
print()

print(x > -5 and x < 5)  # Will print True
print(y > -5 or y < 1)  # Will print True
print(not (x > 0 and x < y))  # Will print False

# Memory and Identity Operators: Memory operators and Identity operators are both used for doing operations on
# objects (lists, dicts, arrays, tuples, etc.). Memory and Identity operators work differently than each other,
# but like Comparative and Logical operators, they will return a True or a False Boolean after the completed
# operation.

# Memory operators include; is (returns True if both variables ARE the same object) and is not (returns True
# if both variables ARE NOT the same object). Now, that functionally sounds a lot like the equal and is not
# equal comparative operators, but there is a slight difference. While equal and is not equal will compare
# the value of the two variables to determine if they are the same, is and is not with look at the variables
# space in memory to determine if they are the same.

# Examples of Memory Operators:

print()
print("~~~~ Memory Operators ~~~~")
print()

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # Will print True
print(a is b)  # Will print False
print(a is not c)  # Will print False
print(a is c)  # Will print True
print(b is not c)  # Will print True

# Identity operators include; in (returns True if a sequence with the specified value IS present in the object)
# and not in (returns True if a sequence with the specified value IS NOT present in the object). What that means
# is we use identity operators to determine if a value is present inside of another variable, for example, is
# a value present in the list or not.

# Examples of Identity Operators:

print()
print("~~~~ Identity Operators ~~~~")
print()

print(a)  # Will print [1, 2, 3]
print(x)  # Will print 1
print(x in a)  # Will print True
print(x not in a)  # Will print False
print()
