import requests
from datetime import datetime as dt

TOKEN = "hfksk2727dndj"
USERNAME = "densol96"
## Create User Account
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

## Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
body_params = {
    "id": "graph1",
    "name": "Studying",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=body_params, headers=headers)
# print(response.text)

pixel_update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"


# date = str(dt.now()).split()[0].split("-")
# formatted_date = "".join(date)

today = dt.now()

# request_body = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": input("Enter the quantity(integers exp): "),
# }

# response = requests.post(url=pixel_update_endpoint, headers=headers, json=request_body)
# print(response.text)

date = input("Choose a date (yyyyMMdd): ")
update_endpoint = f"https://pixe.la/v1/users/densol96/graphs/graph1/{date}"

request_body = {"quantity": input(f"Edit the quantiny on {date}")}

response = requests.put(url=update_endpoint, json=request_body, headers=headers)
print(response.text)
