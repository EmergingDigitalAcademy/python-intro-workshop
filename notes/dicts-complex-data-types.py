# ~~~~~~ Complex Data Types Dicts ~~~~~~ #

# Complex data types don't just hold data like variables do, rather they hold collections of data
# in various formats

# There are a few different complex data types in Python, but we are only going to look at two:
# Lists and Dictionaries

# Dictionaries: Dictionaries are a collection of data wrapped in curly brackets ( {} ),
# that are defined by key value pairs

# A key is used to identify the data within the dictionary, and as the name suggests, a value holds the value
# of the item. A dictionary key MUST be defined with quotes and followed with a colon ( : )
# to list the value for the key

# Different key value pairs within the dictionary are separated by commas ( , )

# Dictionaries can hold many data types, including all of the primitive data types we talked about, lists
# or even other dictionaries!

# Example of a dictionary:

print()
print("~~~~ Print a Dict ~~~~")
print()

person = {
    "name": "Mason",
    "age": 22,
    "height": 6.25,
    "softwareDeveloper": True,
    "hobbies": ["Coding", "Reading", "Gaming"],
}

print(
    person
)  # Print out the dictionary, willl print {'name': 'Mason', 'age': 22, 'height': 6.25, 'softwareDeveloper': True, 'hobbies': ['Coding', 'Reading', 'Gaming']}

# Access Data: There are many ways in Python to access data out of a dictionary, using square brackets ( [] )
# or using the .get() method to access a single key

# Accessing a single key: The simplest way to retrieve data out of a dictionary is by accessing the dicitonary
# variable and including the key name as a string inside of the brackets. This works great, however,
# if you try to access a key that doesn't exist on the dictionary, Python will throw an error.

# This is where the .get() method comes in handy. The .get() method works similarly to using square brackets,
# except it will return None (None is a special data type that indicates no data) instead of throwing an error

# Examples of accessing a single key:

print()
print("~~~~ Print keys in a Dict ~~~~")
print()

print(person["name"])  # Square brackets, will print "Mason"
print(person.get("name"))  # .get() method, will also print "Mason"

# print(person["salary"])  # Will throw an error and break our script, KeyError: 'salary'
print(person.get("Salary"))  # Will NOT throw a KeyError, will print None instead

# Modifying Data: Adding and deleting data out of a dictionary is as simple as calling the
# dictionary and the key you want to modify in square brackets, then either using the del keyword to delete
# data out of the dictionary, or using the equals (=) operator to add new data or change existing data

# Adding / Editing Data: To add data to a dictionary, all you have to do is call the dictionary and follow it
# with a pair of brackets that includes the new key name of the key value you want to add. Then include an
# equals operator (=) to set the value. To edit existing data, follow the same format, but use an existing key
# that already lives on the dictionary

# Examples of adding and editing data:

print()
print("~~~~ Adding Data ~~~~")
print()

person[
    "favoriteSnack"
] = "Cereal"  # I am creating a new "favoriteSnack" key on the person dictionary with value of "Cereal"
print(person["favoriteSnack"])  # Will print "Cereal"

person[
    "favoriteSnack"
] = "PB&J"  # Editing the "favoriteSnack" key on the person dict to "PB&J"
print(person["favoriteSnack"])  # Will print "PB&J"

# Deleting Data: Deleting data from a dict is very similar to everything we have done so far, excpet we
# include the del keyword before we call the dictionary

# Example of deleting data from a dict:

print()
print("~~~~ Removing Data ~~~~")
print()

del person[
    "favoriteSnack"
]  # Deleting the favoriteSnack key and value from the person dict
print(
    person.get("favoriteSnack")
)  # Note the usage of .get() will print None because the key is deleted
print()
