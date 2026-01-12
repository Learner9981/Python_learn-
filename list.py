from loguru import logger

'''
Q what is list?
A List is a collection which is ordered and changeable. Allows duplicate members.

Q How to create a list?
A List can be created by placing all the items (elements) inside square brackets [], separated by commas.

Q How to access elements in a list?
A List items are indexed and you can access them by referring to the index number.

Q How to change elements in a list?
A You can change the value of a specific item by referring to its index number.

Q How to add elements in a list?
A You can use append() method to add an element at the end of the list. You can use insert() method to add an element 
at the specified position. You can use extend() method to add elements of another list to the end of the current list.

Q How to create a list of lists?
A A list can contain other lists as its elements. This is called a nested list or a list of lists.

'''

labour_name = ["Mahesh", "Mithilesh", "Ramesh", "Sumesh"]

logger.info(f"First element in the list is {labour_name[-1]}")

labour_name.append("Ram")
labour_name.append("Mohan")

labour_name.insert(0,"Babu")

new_labour = ["Sukesh","Pankaj"]
labour_name.extend(new_labour)
logger.info(f"element in the list are {labour_name}")


labour_with_wage = [["Mahesh",500],["Ramesh",400]]

logger.info(f"Labour wage is {labour_with_wage [0][1]}") 
