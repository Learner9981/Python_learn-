from loguru import logger
import math

length_of_land = 100
breadth_of_land = 200
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home =True

length_of_land = int(input("Enter the length of land in ft: "))

if length_of_land <200:
    logger.info(f"Your length is not sufficient to build  5 bhk house")
    if length_of_land <500:
        logger.info(f"You can build 2 building ")
    else:
        logger.info(f"You do not have suffient space")
else:
    logger.info(f"Share more details")    


#How will you find out if given number by user is even or odd

user_input_number = int(input("Enter a number: "))

if user_input_number % 2 == 0:
    logger.info(f"The number is even")
else:
    logger.info(f"the no is odd")