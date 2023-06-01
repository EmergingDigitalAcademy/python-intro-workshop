# ~~~~~~ Complex Data Types Lists ~~~~~~ #

# Complex data types don't just hold data like variables do, rather they hold collections of data
# in various formats

# There are a few different complex data types in Python, but we are only going to look at two:
# Lists and Dictionaries

# Lists: Lists are a collection of data surrounded by square brackets ( [] ) and separated by commas ( , )
# Lists are heterogenous, meaning they can hold variety of data types, and the data within the list is mutable
# meaning that the content of the data can change without changing the identity of the data.

# Examples of lists:

listOne = ["a", "b", "c", "d"]
listTwo = [0, 1, 2, 3, 4]
listThree = ["a", 0, 3.14, True]

# Access Data: We can access the data within a list by calling the variable the list is stored in,
# followed by a set of square brackets directly after that will hold the index position of the list
# item we want to access.

# Index Positioning: The position of an item within a list is called it's index. Indexing always starts at 0,
# so an item at the first position inside of a list will have an index of 0, the second item will have an
# index of 1, third item will have an index of 2, etc.

# Examples of accessing data within a list:

print()
print("~~~~ Access Data in a List ~~~~")
print()

print(listTwo[0])  # Will print 0
print(listOne[1])  # Will print "b"
print(listThree[3])  # Will print True

# Modifying Data: There are two ways that we can both add and remove data. The first way we add data is with the
# .append() list method. (All of our data types include built in methods, a method is a function that can only
# be used on the item it was created on. For example, .append() can only be called on lists as it is a list
# method.) The .append() will add whatever you include in the parenthesis to the end of our list.

# The second way to add data to a list is with the .insert() list method. The .append() and .insert() methods
# functionally work almost identical, however while .append() will add data to the end of a list, .insert()
# will add data to the index we specify, and will shift everything behind the inserted data to the right.

# Examples of adding data to a list:

print()
print("~~~~ Add Data to a List ~~~~")
print()

listOne.append("e")  # Will add "e" to the end of listOne
print(listOne)  # Will print ['a', 'b', 'c', 'd', 'e']

listTwo.insert(
    0, -1
)  # Will add -1 to listThree at index 0 and move everything existing one index right
print(listTwo)  # Will print [-1, 0, 1, 2, 3, 4]

# We can delete data from a list by using the .remove() method. The .remove() method works like .append()
# and .insert() where it looks at whatever is provided in the parenthesis, and we can provide the item we
# want to remove from the list inside of the parenthesis.

# The second way to remove data is with the .pop() method. The .pop() method will remove the item at the index
# of the list you provide in the parenthesis.

# You would use .remove() in a situation where you knew the item you wanted to remove but not the index,
# and you would use .pop() in the opposite situation, where you knew the index but not the item.


# Examples of removing data from a list:

print()
print("~~~~ Remove Data from a List ~~~~")
print()

listThree.remove(3.14)  # Will remove 3.14 from listThree
print(listThree)  # Will print ['a', 0, True]

listThree.pop(0)  # Will remove "a" from listThree
print(listThree)  # Will print [0, True]
print()
