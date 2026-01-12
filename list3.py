from loguru import logger

'''I have a sorted list and need ot insert the new value in sucha way that after inserting the element the list remains sorted


create a new variable name index
find out the index loocation -> for loop comparison 
'''

index = 0 
num_to_insert = 55

lst= [5,18,77,108,930]

for num in lst:
    if num > num_to_insert:
        index=index
        break
    else:
        index=index+1    

lst.append(None)
for i in range(len(lst) - 1, index, -1):
    lst[i] = lst [i-1]
    lst[index] = num_to_insert