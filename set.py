'''
Q1. What is set?
A set is a built-in Python data type that stores a collection of unique elements in an unordered way.

1. Feature of set in python?
unordered, immutable, cannot contain duplicate entry
2. set in maths?

3. Methods of set in python 

4. Iteration in set

'''
from loguru import logger

# List = []
# Dictionary = {} # Key-value pair
# Tuple = ()
# set = {} # only value no key 

# set_var = {} # this will be considered as empty dictionary not set
# print(type(set_var))

# set1_var = set() # to create a empty set we need to use this 
# print(type(set1_var))

# set_var = {1,2,7,8,4,12}
# new_set_var = {2,4,6,5,15}

# print(set_var.union(new_set_var))
# print(set_var.intersection(new_set_var))
# print(set_var.difference(new_set_var))
# print(set_var.symmetric_difference(new_set_var))
# print(set_var.isdisjoint(new_set_var))

'''Q1. Given two lists, find the missing and additional values in both the list.
Input: 
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]
output :
Missing values in list1= [8,7]
Additional values in list1 = [1,2,3]
Missing values in list2 = [1,2,3]
Additional values in list 2 = [7,8]
'''
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]

t1 = set(list1)
t2 = set(list2)

print(f"Missing values in list1 = { t2.difference(t1)}")
print(f"Additional values in list1 = { t1.difference(t2)}")
print(f"Missing values in list2 = { t1.difference(t2)}")
print(f"Additional values in list2 = { t2.difference(t1)}")
'''
Q2. Given three arrays we have to find common elements in 3 sorted list using sets.

Input: 
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

Output = [80,20]

'''

arr1 = [1,5,10,20,40,80]
arr2 = [6,7,20,80,100]
arr3 = [3,4,15,20,30,70,80,120]

common_items_in_arr = set(arr1).intersection(set(arr2),set(arr3))

print(common_items_in_arr)