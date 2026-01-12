'''
Docstring for list_comp

Q1. Why do we need list comprehension?
List comprehension provides a concise way to create lists. It is more readable and often faster than using traditional loops 
for creating lists.
Q2 Where do we use in real world applications ?
List comprehensions are widely used in data processing, web development, and any scenario where you need
to transform or filter data efficiently.
'''

from loguru import logger

# new_list = []
# for i in range(1,11):
#     if i % 2 ==0:
#         new_list.append(i)
# print(new_list)        
  

# new_list = [i for i in range(1,11) if i%2==0]

# print(new_list)

new_list = []
for i in range(1,11):
    if i % 2 ==0:
        new_list.append("Even")
    else:
        new_list.append("Odd")
print(new_list)
  

new_list = ["Even" if i%2==0 else "Odd" for i in range(1,11)]
print(new_list) 