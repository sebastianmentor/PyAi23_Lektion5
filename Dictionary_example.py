"""Dictionaries in Python are versatile and powerful data 
structures that can be used to store key-value pairs. 
Here are several examples to demonstrate various features 
and uses of dictionaries:
"""
# 1. **Basic Dictionary Creation**

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}


# 2. **Accessing Values**

print(person["name"])  # Outputs: Alice


# 3. **Using `get()` to Access Values**

print(person.get("age"))  # Outputs: 30
print(person.get("country", "USA"))  # Outputs: USA


# 4. **Adding/Updating Key-Value Pairs**

person["job"] = "Engineer"
person["age"] = 31

# 5. **Deleting a Key-Value Pair**

del person["city"]


# 6. **Iterating Through a Dictionary**

for key, value in person.items():
    print(key, ":", value)


# 7. **Checking if a Key Exists**
if "name" in person:
    print("Name is present!")


# 8. **Dictionary Comprehension**

squares = {x: x*x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# 9. **Merging Two Dictionaries** (Python 3.9 and later)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2  # {'a': 1, 'b': 3, 'c': 4}


# 10. **Nested Dictionaries**

family = {
    "child1": {"name": "Bob", "age": 12},
    "child2": {"name": "Eve", "age": 9}
}

print(family["child1"]["name"])  # Outputs: Bob

# 11. **Dictionary Length**

print(len(person))  # Outputs number of key-value pairs


# 12. **Removing Items Using `pop()`**

age = person.pop("age")
print(age)  # Outputs: 31


# 13. **Clearing All Items**

person.clear()

"""
These are just a few examples of what you can do with 
dictionaries in Python. Depending on your use case, 
you can leverage other methods and techniques to manipulate
and utilize dictionaries effectively.
"""