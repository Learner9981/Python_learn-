'''
Q1. Types of argument in python function?
1. posititional argument
2. Arbitary argument ->args
3. Default argument
 *args?
Q3. what is **kwargs ?
'''


from loguru import logger



def final_cart_amount(discount,*args):
    result = 0 
    for amount in args:
        result+=amount
    print(result)

    amount_after_discount = result - (result*discount)

    return amount_after_discount

final_amount_to_be_paid = final_cart_amount(0.5,100,500,100,300,500)

logger.info(final_amount_to_be_paid)

''' 
Q1. Write a program where you need to take N numbers of inputs from user and return the total sum of it

Q2. Write a program in which function takes logs input from the user and write this into a file'''