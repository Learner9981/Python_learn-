'''
Q1. what is functional programming ?
Q2. what is modular programming?
Q3. why do we need functino?
Q4. How function works?
'''
from loguru import logger

def calculate_fencing_cost(length,breadth,cost_per_ft):
    circumference = 2 * (length + breadth)
    cost_for_fencing = circumference * cost_per_ft
    return cost_for_fencing

cost_for_fencing_land = calculate_fencing_cost(length_of_land,breadth_of_land,17) 

logger.info(f"fencing cost for the land is {cost_for_fencing_land}")