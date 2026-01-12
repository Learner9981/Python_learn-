'''
Docstring for dictionry
Q1. what is the use case of dictionary in real time ?
Dictionaries are used to store data values in key-value pairs, allowing for efficient data retrieval based on unique keys. They are commonly used in applications such as databases, caching, and configuration settings.
Q2. How to create dicitonary?
Dictionaries can be created using curly braces {} with key-value pairs separated by commas, or by using the dict() constructor.
Q3. How to update dictionary?
Dictionaries can be updated by adding new key-value pairs or modifying existing ones using the assignment operator. You can also use methods like update() to merge another dictionary.
Q4. How to iterate?
Dictionaries can be iterated using loops such as for loops. You can iterate over keys, values, or key-value pairs using methods like keys(), values(), and items().
Q5. How to delete elements from dictionary?
Elements can be deleted from a dictionary using the del statement, the pop() method to remove a specific key, or the clear() method to remove all items.
Q6. How to nested dictionary?
A nested dictionary is a dictionary that contains another dictionary as a value. It can be created by assigning a dictionary to a key in another dictionary.
Q7. How to copy dictionary?
Dictionaries can be copied using the copy() method or the dict() constructor to create a shallow copy. For deep copies, the copy module's deepcopy() function can be used.
Q8. How to merge two dictionaries?
Two dictionaries can be merged using the update() method, the {**dict1, **dict2} syntax, or the | operator (in Python 3.9 and later) to create a new dictionary containing keys and values from both.

Q9 what are the commonly used methods in dictionary ?
- keys(): Returns a view object containing the keys of the dictionary.
- values(): Returns a view object containing the values of the dictionary.
- items(): Returns a view object containing the key-value pairs of the dictionary.
- get(key, default): Returns the value for the specified key if it exists, otherwise returns the default value.
- pop(key, default): Removes the specified key and returns its value. If the key does not exist, returns the default value.
- update([other]): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.

Q10. Dictionary comprehension?
Dictionary comprehension is a concise way to create dictionaries using a single line of code. It follows the
syntax: {key_expression: value_expression for item in iterable if condition}.

Q11. In method in method ?
Answer: The in method is used to check if a key exists in a dictionary. It returns True if the key is found, otherwise False.

'''
from loguru import logger

# Creating a dictionary
labour_with_cost = {"Mahesh":500,"Mithilesh":400,
                    "Ramesh":400,"Sumesh":300,
                    "Jagmohan":1000,"Rampyare":800
                    }

# labour_with_cost["Jagmohan"] = 1000 # Adding new key-value pair
# labour_with_cost["Rampyare"] = 800 # Adding new key-value pair

# logger.info(f"Labour keys are {labour_with_cost.keys()}") # Iterating over keys
# logger.info(f"Labour values are {labour_with_cost.values()}") # Iterating over values
# logger.info(f"Labour items are {labour_with_cost.items()}") # Iterating over key-value pairs


# for name in labour_with_cost: #` Iterating over keys. default gives keys
#     logger.info(f"{name},{labour_with_cost[name]}")

# for key,value in labour_with_cost.items(): # Iterating over key-value pairs
#     logger.info(f"{key},{value}") 

# logger.info(f"{labour_with_cost}")

# GET Method and in method
# print(labour_with_cost.get("Mahesh1")) # Accessing value using get method
# print(labour_with_cost["Mahesh1"]) # Accessing value using key


#KEY and values 
# print(labour_with_cost.keys())
# print(labour_with_cost.values())

# Item method
# print(labour_with_cost.items())

#Update method
# labour_with_cost.update({"Pawan":1200, "Rahul": 900}) # Updating dictionary with new key-value pair
# new_labour = {"Pawan":1200, "Rahul": 900}
# final_labour = {**labour_with_cost,**new_labour} # Merging two dictionaries
# print(final_labour)
# # print(labour_with_cost)


# pop method
# print(labour_with_cost.pop("Mahesh")) # Removing key-value pair using pop method
# print(labour_with_cost.popitem())
# print(labour_with_cost.popitem())
# print(labour_with_cost.keys())

#copy method
# new_labour = labour_with_cost.copy() 
# print(id(new_labour))
# print(id(labour_with_cost))

# clear method
# labour_with_cost.clear()
# print(labour_with_cost)

#delete method
# del labour_with_cost["Mahesh"]
# print(labour_with_cost)

# Dictionary Comprehension
# labour_with_cost = {key:labour_with_cost[key]+100 for key in labour_with_cost}
# print(labour_with_cost)

# labour_with_cost = {Key: labour_with_cost.get(Key) +100 if Key!="Jagmohan" else labour_with_cost.get(Key) for Key in labour_with_cost}
# print(labour_with_cost)


print(len(labour_with_cost))


# #in method


# name = "Pawan"

# letter_count = {}
# for char in name:
#     if char in letter_count:
#         letter_count[char] = letter_count[char] + 1
#     else:
#         letter_count[char] = 1
#         print(letter_count)
# # print(letter_count)        