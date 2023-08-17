import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

URI = "https://pixe.la/v1/users"
USERNAME = os.environ["user"]
GRAPH_ID = "graph01"


def create_account():
    params = {
        "token": os.environ["api_token"],
        "username": os.environ["username"],
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=URI, json=params)
    print(response.text)


def create_graph():
    create_graph_endpoint = f"{URI}/{USERNAME}/graphs"

    params = {
        "id": GRAPH_ID,
        "name": "Programming Graph",
        "unit": "Lessons",
        "type": "int",
        "color": "kuro",

    }

    headers = {
        "X-USER-TOKEN": os.environ["api_token"],
    }

    response = requests.post(url=create_graph_endpoint, json=params, headers=headers)
    print(response.text)


def add_pixel_to_graph():
    create_graph_endpoint = f"{URI}/{USERNAME}/graphs/{GRAPH_ID}"
    today_string = datetime.now().date().strftime("%Y%m%d")
    params = {
        "date": today_string,
        "quantity": "2",
    }

    headers = {
        "X-USER-TOKEN": os.environ["api_token"],
    }

    response = requests.post(url=create_graph_endpoint, json=params, headers=headers)
    print(response.text)


def update_graph():
    today_string = datetime.now().date().strftime("%Y%m%d")
    create_graph_endpoint = f"{URI}/{USERNAME}/graphs/{GRAPH_ID}/{today_string}"

    params = {
        "quantity": "17",
    }
    headers = {
        "X-USER-TOKEN": os.environ["api_token"],
    }
    response = requests.put(url=create_graph_endpoint, json=params, headers=headers)
    print(response.text)


def delete_pixel_in_graph():
    today_string = datetime.now().date().strftime("%Y%m%d")
    create_graph_endpoint = f"{URI}/{USERNAME}/graphs/{GRAPH_ID}/{today_string}"

    headers = {
        "X-USER-TOKEN": os.environ["api_token"],
    }
    response = requests.delete(url=create_graph_endpoint, headers=headers)
    print(response.text)

add_pixel_to_graph()
