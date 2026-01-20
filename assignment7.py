'''Calculate the cost of books bought by each student

book_name,Cost
science,262
math,178
history,59
physics,231
biology,165
chemistry,110

student_details = {1:["Math","History"],
                   2:["Biology","chemistry","history"],
                   3:["science"]}

save the book cost details in ini File

b. what will be the cost for books if discount is 10%. but the condition to get discount is, you will have to buy 2 or more books.'''

from loguru import logger
import configparser

# using the configparser to load the book cost from ini file
config = configparser.ConfigParser()
config.read(r"C:\Users\Pawan\Desktop\DataEngineeringProject\Python\Python_learn-\books.ini")

#converting the value into int
book_cost = {book: int(cost) for book, cost in config["books"].items()}

student_details = {"Akshay":["Math","History"],
                   "Manish":["Biology","chemistry","history"],
                   "Pawan":["science"]
                  }
#function to calculate the total cost 
def calculate_cost(student_books):
    total = sum(book_cost[book.lower()] for book in student_books) 
# apply discount if 2 or more books purchased
    if len(student_books)>=2:
        total *= 0.9 #10% discount
    return total

# calculate for each student 
for std_id,books in student_details.items():
    cost = calculate_cost(books)
    logger.info(f"{std_id} bought {books}, Total cost = {cost}")