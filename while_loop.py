'''
Docstring for while_loop

Q1. Why do we need while loop?



Q2 Where do we use in real world applications ?
'''
from loguru import logger
import time

labour_name = ["Mahesh", "Ramesh", "Suresh", "Dinesh"]

name_iter = len(labour_name)-1
while (name_iter >= 0):
    print(labour_name[name_iter])
    time.sleep(5)
    name_iter -= 1