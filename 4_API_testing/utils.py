import requests

# def status_code(url):
#     response = requests.get(url)
#     return response.status_code
#
# def response_data_content(url):
#     response = requests.get(url)
#     response = response.json()
#     return response, [*response]
#
# def p3_requests(url, body):
#     response = requests.post(url, body)
#     return [*response.json()][0]




USER_BODY = {'email':'Ann@gmail.com',
                # 'username':'Annabel',
                # 'password':'A4/nabel@',
                # 'name':{
                #     'firstname':'Annabel',
                #     'lastname':'Garsia'
                # },
                # 'address':{
                #     'city':'Genua',
                #     'street':'7835 new road',
                #     'number':3,
                #     'zipcode':'32926-3874',
                #     'geolocation':{
                #         'lat':'-57.3159',
                #         'long':'81.1496'
                #     }
                # },
                # 'phone':'5-570-236-7033'
             }
response = requests.post("https://fakestoreapi.com/users", USER_BODY)
print([*response.json()][0])
