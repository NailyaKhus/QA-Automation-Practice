import requests

def status_code(url):
    response = requests.get(url)
    return response.status_code

def response_data_content(url):
    response = requests.get(url)
    response = response.json()
    return response, [*response]

def p3_requests(request_word, url, body):
    if request_word == 'post':
        response = requests.post(url, body)
    elif request_word == 'put':
        response = requests.put(url, body)
    elif request_word == 'patch':
        response = requests.patch(url, body)
    return [*response.json()]
