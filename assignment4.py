'''
Assignment 4: Dictionary Operations
This file contains the implementation of dictionary operations.

Q Calculate the total labour cost if total working days was 50 days.
out of which Mahesh was absent for 3 days and Jagmohan was absent for 7 days
find out the total cost incurred to the company towards labour payment.    

'''

from loguru import logger

# Creating a dictionary
labour_with_cost = {"Mahesh":500, 
                    "Mithilesh":400,
                    "Ramesh":400, 
                    "Sumesh":300
                    ,"Jagmohan":1000
                    ,"Rampyare":800}

no_of_days = 50
total_cost = 0

for cost in labour_with_cost:
    total_cost = total_cost + labour_with_cost[cost]

total_cost = (total_cost * no_of_days) - ((7*(labour_with_cost["Mahesh"])) + (4 * (labour_with_cost["Jagmohan"]))) 
logger.info(f"Total labour cost incurred to the company is {total_cost}")