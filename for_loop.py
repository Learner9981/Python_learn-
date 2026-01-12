from loguru import logger


logger.info("Programming is easy")

labour_name = ["Mahesh", "Mithilesh", "Ramesh", "Sumesh"]


# for name in labour_name:
#     logger.info(f"Labour name is {name}")

# for i in range(5,10):
#     logger.info(f"Value of i is {i}")

for i in range (len(labour_name)):
    logger.info(f"Labour {i+1} name is {labour_name[i]}")



