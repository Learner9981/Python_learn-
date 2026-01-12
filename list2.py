from loguru import logger


labour_name = ["Mahesh", "Mithilesh", "Ramesh", "Sumesh",500,400,500,300]

# print(labour_name[::-1])

labour_name.insert(4,"Ramu")

labour_name.append(600)

print(labour_name)

api_endpoint = "https://apipheny.io/post-request-google-sheets/"

new_api = api_endpoint.split("-")

print(new_api[-1])