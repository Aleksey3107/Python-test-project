import requests
import json


def send_request():
    request = requests.get(url='http://192.168.10.20:1341/v2/recs/core?', params='locale=en')
    return request


def retrieve_data(response):
    data = json.loads(response.text)
    for i, j in data.items():
        if i == 'data':
            users_coll = j
            return users_coll


def aggregate_user_data(user_data):
    dataset = json.dumps(list(user_data.values()))
    users_collection = dataset.split('"type": "user", ')
    users = []
    for i in users_collection:
        users.append(i)
    users.pop(0)
    return users