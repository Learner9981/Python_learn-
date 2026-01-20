'''
Docstring for tuple
Q1. What is a tuple in Python?
A tuple is an immutable, ordered collection of elements in Python. It is similar to a list, but unlike lists, tuples cannot be modified after their creation.
Q2. How to create a tuple?  
Tuples can be created by placing a comma-separated sequence of values inside parentheses (). For example: my_tuple = (1, 2, 3).
Q3. How to access elements in a tuple?
Elements in a tuple can be accessed using indexing, similar to lists. The index starts at 0 for the first element. For example: my_tuple[0] will access the first element.
Q4. How to slice a tuple?
Tuples can be sliced using the same syntax as lists. You can specify a start index, an end index, and an optional step. For example: my_tuple[1:4] will return a new tuple containing elements from index 1 to 3.
Q5. How to concatenate tuples?
Tuples can be concatenated using the + operator. For example: tuple1 + tuple2 will create a new tuple that combines the elements of both tuples.
Q6. How to unpack a tuple?  
Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single statement. For example: a, b, c = my_tuple will assign the first element to a, the second to b, and the third to c.
Q7. How to iterate over a tuple?
You can iterate over a tuple using a for loop. For example: for item in my_tuple: print(item) will print each element in the tuple.
Q8. How to find the length of a tuple?
You can find the length of a tuple using the len() function. For example: len(my_tuple) will return the number of elements in the tuple.
Q9. Are tuples mutable or immutable?
Tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed.
Q10. What are some common use cases for tuples?
Tuples are often used to group related data together, such as coordinates (x, y), RGB color values (r, g, b), or to return multiple values from a function. They are also used when immutability is required for data integrity.

Q11. features of tuples?
- Immutable: Tuples cannot be modified after creation.
- Ordered: Tuples maintain the order of elements.
- Allow Duplicates: Tuples can contain duplicate elements.
- Heterogeneous: Tuples can contain elements of different data types.

Q12. Methods available in set ?
Tuples have only two built-in methods:
- count(): Returns the number of occurrences of a specified value in the tuple.
- index(): Returns the index of the first occurrence of a specified value in the tuple.

Q13.slicing and in method ?
Tuples support slicing to extract a portion of the tuple using the syntax tuple[start:end:step]. The 'in' method can be used to check if an element exists in the tuple, returning True or False.
'''

from loguru import logger

# test_tuple = (1, 2, 45,6,2,143,"True","Pawan",2,True)
# test_tuple[2] = 5  # This will raise a TypeError since tuples are immutable

# new_tuple = (2) # This is not a tuple, it's an integer if we create single valued it will consider it it as a constant value
# if 1 in test_tuple:
#     logger.info("Element is present in the tuple")

# logger.info(f"{test_tuple[2:7]}")  # Slicing the tuple
# logger.info(f"{test_tuple.count(2)}")  # Counting occurrences of 2
# logger.info(f"{test_tuple.index(2)}")  # Finding index of first occurrence of 2
# logger.info(f"Length of the tuple is {len(test_tuple)}")  # Length of the tuple
# new_tuple = (2,)  # This is a tuple with a single element
# print(type(new_tuple))

'''
Tuple questions 
Q1 Write a program to return entire elemenets as a tuple which can have a list in the tuple inputs ?
Example -:
Input:- test_tuple = ([5,6],[6,7,8,9], [3])
Output:- (5,6,6,7,8,9,3)
Also mention about the time and space complexity ?
'''
# result = []

# test_tuple = ([5,6],[6,7,8,9], [3])

# for lst in test_tuple:
#     result.extend(lst)

# print(result)  



'''
Q2. Write a program to return a tuple which is exponential of given two tuples as an input 

Example:- 

Input:- tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)
Output:- (1000,64,81,125))
'''

result = []
tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)


for number in range(len(tuple1)):
    result.append(tuple1[number] ** tuple2[number])

final_tuple = tuple(result)
print(final_tuple)