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
    assert utils.p3_requests(data.BASE_URL+data.URI_USER_LOGIN, body) == 'token'

def test_create_new_user():
    assert utils.p3_requests(data.BASE_URL+data.URI_USERS, data.USER_BODY) == 'id'

# PUT
def test_update_user_data():
    assert utils.p3_requests(data.BASE_URL+)



