import utils
import data
import pytest

# GET
def test_status_code():
    assert utils.response_get(data.BASE_URL).status_code == 200

def test_response_data():
    assert utils.response_get(data.BASE_URL + data.URI_PRODUCT_PATH) != "Nan"

def test_product_content():
    response = utils.response_get(data.BASE_URL + data.URI_PRODUCT_PATH)
    assert [*response.json()] == data.PRODUCT_CONTENT

# POST
@pytest.mark.parametrize("login, password", data.LOGIN_PASSWORD_DICT)
def test_valid_users(login, password):
    body = ({'username': login,
             'password': password})
    response = utils.request_post(data.BASE_URL+data.URI_USER_LOGIN, body)
    assert [*response.json()][0] == 'token'

def test_create_new_user():
    response = utils.request_post(data.BASE_URL+data.URI_USERS, data.USER_BODY)
    assert [*response.json()][0] == 'id'

# PUT
def test_update_user_data_put():
    new_data_key_list = [*data.USER_BODY]
    response = utils.request_put(data.BASE_URL+data.URI_USER_TO_CHANGE, data.USER_BODY)
    assert [*response.json()] == new_data_key_list

def test_update_product_put():
    new_data_key_list = [*data.PRODUCT_BODY]
    response = utils.request_put(data.BASE_URL + data.URI_PRODUCT_PATH, data.PRODUCT_BODY)
    # product's response data comes adding 'id' in the head of the list -
    # what's why we take subsequence of the list in the following string
    assert [*response.json()][1:] == new_data_key_list

# PATCH
def test_update_user_data_patch():
    # Let's assume that only the password is changed
    data_change_index = 2
    new_data_key = list(data.USER_BODY.keys())[data_change_index]
    user_body = dict([list(data.USER_BODY.items())[data_change_index]])
    response = utils.request_patch(data.BASE_URL+data.URI_USER_TO_CHANGE, user_body)
    assert [*response.json()][0] == new_data_key




