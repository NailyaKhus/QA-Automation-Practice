import requests

def response_get(url):
    response = requests.get(url)
    return response

def request_post(url, body):
    response = requests.post(url, body)
    return response

def request_put(url, body):
    response = requests.put(url, body)
    return response

def request_patch(url, body):
    response = requests.patch(url, body)
    return response
