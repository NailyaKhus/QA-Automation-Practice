BASE_URL = "https://fakestoreapi.com"
URI_PRODUCT_PATH = "/products/1"
URI_USER_LOGIN = "/auth/login"
URI_USERS = '/users'
URI_USER_TO_CHANGE = '/users/1'
PRODUCT_CONTENT = ['id', 'title', 'price', 'description', 'category', 'image', 'rating']
LOGIN_PASSWORD_DICT = [("mor_2314","83r5^_"),("johnd","m38rmF$"), ("kevinryan","kev02937@")]

USER_BODY = {'email':'Ann@gmail.com',
                'username':'Annabel',
                'password':'A4/nabel@',
                'name':{
                    'firstname':'Annabel',
                    'lastname':'Garsia'
                },
                'address':{
                    'city':'Genua',
                    'street':'7835 new road',
                    'number':3,
                    'zipcode':'32926-3874',
                    'geolocation':{
                        'lat':'-57.3159',
                        'long':'81.1496'
                    }
                },
                'phone':'5-570-236-7033'}

PRODUCT_BODY = {'title': 'some_product',
                'price': 135,
                'description': 'item for kitchen',
                'image': 'https://whatever.net',
                'category': 'electronic'}

INCORRECT_PRODUCT_URI_LIST = ["0","-1", "o", "!", "1.1"]

INCORRECT_PRODUCT_BODY_LIST = ["", {}, "NaN", "Hi, how are you?", {'NaN'}, {"NaN": "NaN"}]