import requests
from datetime import datetime as dt
import time


class Manager:
    def __init__(self):
        # self.username = input("Provide a unique username: ")
        self.username = "den4iks"
        self.id = ""
        # self.token = self.get_user_info()
        self.token = ""
        self.headers = {"X-USER-TOKEN": ""}

    def get_user_info(self):
        check = True
        int_found = False
        letter_found = False
        counter = 0
        while check:
            token = input(
                "Provide a token that starts with a letter and contains at least 1 digit; 8-22 long: "
            )
            if 8 <= len(token) <= 22 and token[0].isalpha():
                for character in token:
                    if counter == 2:
                        check = False
                        break
                    elif character.isdigit() and not int_found:
                        counter += 1
                        int_found = True
                    elif character.isalpha() and not letter_found:
                        counter += 1
                        letter_found = True
                if check:
                    print("Token input is wrong! Try again!")
            else:
                print(
                    "It should be between 8-22 characters long and start with a letter!"
                )

        print("Thank you for providing correct information!")
        return token

    def check_response(self, response, function):
        print(response.status_code)
        print(response.text)
        if response.status_code == 200:
            return True, response.text
        elif response.status_code == 503:
            return function()
        else:
            return False, response.text

    def create_user(self):
        pixela_endpoint = "https://pixe.la/v1/users"
        user_params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        response = requests.post(url=pixela_endpoint, json=user_params)
        return self.check_response(response, self.create_user)

    def create_graph(self):
        graph_endpoint = f"https://pixe.la/v1/users/{self.username}/graphs"

        body_params = {
            "id": self.id,
            "name": "Studying",
            "unit": "minutes",
            "type": "int",
            "color": "shibafu",
            "timezone": "Europe/Moscow",
        }

        response = requests.post(
            url=graph_endpoint, json=body_params, headers=self.headers
        )

        return self.check_response(response, self.create_graph)

    def update_graph(self, quantity_value):
        pixel_update_endpoint = (
            f"https://pixe.la/v1/users/{self.username}/graphs/{self.id}"
        )
        today = dt.now()
        date = today.strftime("%Y%m%d")
        request_body = {"date": date, "quantity": quantity_value}
        response = requests.post(
            url=pixel_update_endpoint, headers=self.headers, json=request_body
        )

        return self.check_response(response, self.update_graph)

    def edit_graph(self):
        date = input("Choose a date (yyyyMMdd): ")
        edit_endpoint = (
            f"https://pixe.la/v1/users/{self.username}/graphs/{self.id}/{date}"
        )
        print(1)
        request_body = {
            "quantity": input(f"Edit the amount of minutes on {date} ---> ")
        }
        print(2)
        response = requests.put(
            url=edit_endpoint, json=request_body, headers=self.headers
        )
        print(3)
        return self.check_response(response, self.edit_graph)

    def delete_from_graph(self):
        date = input("Choose a date (yyyyMMdd): ")
        delete_endpoint = (
            f"https://pixe.la/v1/users/{self.username}/graphs/{self.id}/{date}"
        )
        response = requests.delete(url=delete_endpoint, headers=self.headers)

        return self.check_response(response, self.delete_from_graph)

    def delete_user(self, username=None, header=None):
        if username is None:
            username = self.username
        if header is None:
            header = self.headers
        delete_user_endpoint = f"https://pixe.la/v1/users/{username}"
        response = requests.delete(url=delete_user_endpoint, headers=header)
        if response.status_code == 200:
            return True
        return False
