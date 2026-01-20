'''
Docstring for error_handle
what is exceptional handling
why do we need
when to raise exception and when not to.
Write a program to open a file if file is empty then raise an exception.
if it's not empty then find out all of the unique names in the file.
'''

from loguru import logger



def final_cart_amount(*args,discount = 0.1):
    try:
        result = 0 
        for amount in args:
            result+=amount
        print(result)

        amount_after_discount = result - (result*discount)

        return amount_after_discount
    except NameError:
        logger.info("Variable not found")
        raise Exception("Please check the variable name")
    except TypeError :
        logger.info("Please provide the amount in integer")
        raise Exception("Value provided is not an integer coming from TypeError")
    except Exception as e:
        logger.info("cannot process the cart amount")
        raise e

final_amount_to_be_paid = final_cart_amount(100,500,100,300,'500',discount = 0.5)

logger.info(final_amount_to_be_paid)

logger.info("Entry in database done. job ran successsfully " )