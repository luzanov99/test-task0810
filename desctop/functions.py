import requests

def update_app():
    url="http://193.122.78.15/api/ver1/events/all"
    headers ={'Authorization': 'Token b7e62e054daaab8c4cefb93027989bbd9a762261'}
    response = requests.get(url, headers=headers)
    return response.json()
    



