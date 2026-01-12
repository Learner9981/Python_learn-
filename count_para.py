from loguru import logger

print("Programming is easy")

count = 0

paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimensional approach.
He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the first commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University """

para_list = paragraph.lower().split(" ")

# print(para_list)

for letter in para_list:
    if letter == "the":
        count = count+1
    else:
        continue

logger.info(f"Total count for \"the\" article is {count}")        

