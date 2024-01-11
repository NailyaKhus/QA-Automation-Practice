import utils
import data
import pytest

# GET
def test_status_code():
    assert utils.status_code(data.BASE_URL) == 200

def test_response_data():
    res, _ = utils.response_data_content(data.BASE_URL + data.URI_PRODUCT_PATH)
    assert res != "Nan"

def test_product_content():
    _, content_list = utils.response_data_content(data.BASE_URL + data.URI_PRODUCT_PATH)
    assert content_list == data.PRODUCT_CONTENT

# POST
@pytest.mark.parametrize("login, password", data.LOGIN_PASSWORD_DICT)
def test_valid_users(login, password):
    body = ({'username': login,
             'password': password})
    assert utils.p3_requests('post', data.BASE_URL+data.URI_USER_LOGIN, body)[0] == 'token'

def test_create_new_user():
    assert utils.p3_requests('post', data.BASE_URL+data.URI_USERS, data.USER_BODY)[0] == 'id'

# PUT
def test_update_user_data_put():
    new_data_key_list = [*data.USER_BODY]
    assert utils.p3_requests('put', data.BASE_URL+data.URI_USER_TO_CHANGE, data.USER_BODY) == new_data_key_list

def test_update_product_put():
    new_data_key_list = [*data.PRODUCT_BODY]
    # product's response data comes adding 'id' in the head of the list -
    # what's why we take subsequence of the list in the following string
    assert utils.p3_requests('put', data.BASE_URL + data.URI_PRODUCT_PATH, data.PRODUCT_BODY)[1:] == new_data_key_list

# PATCH
def test_update_user_data_patch():
    # Let's assume that only the password is changed
    data_change_index = 2
    new_data_key = list(data.USER_BODY.keys())[data_change_index]
    user_body = dict([list(data.USER_BODY.items())[data_change_index]])
    assert utils.p3_requests('patch', data.BASE_URL+data.URI_USER_TO_CHANGE, user_body)[0] == new_data_key




