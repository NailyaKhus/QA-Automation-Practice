import requests

def status_code(url):
    response = requests.get(url)
    return response.status_code

def response_data_content(url):
    response = requests.get(url)
    response = response.json()
    return response, [*response]

def login_user(url, username, password):
    body = ({'username': username,
             'password': password})
    response = requests.post(url, body)
    response = response.json()
    return([*response])

