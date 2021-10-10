import requests
from config import *
def update_app():
    url=URL_HUB
    headers ={'Authorization': 'Token '+URL_TOKEN}
    response = requests.get(url, headers=headers)
    return response.json()
    

def get_info_server():
    url=URL_SERVER
    response = requests.get(url)
    return response.json()
