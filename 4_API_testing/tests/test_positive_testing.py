import utils
import data
import pytest

# GET
def test_status_code():
    assert utils.status_code(data.BASE_URL) == 200

def test_response_data():
    res, _ = utils.response_data_content(data.BASE_URL + data.PRODUCT_PATH)
    assert res != "Nan"

def test_product_content():
    _, content_list = utils.response_data_content(data.BASE_URL + data.PRODUCT_PATH)
    assert content_list == data.PRODUCT_CONTENT

# POST
@pytest.mark.parametrize("login, password", data.LOGIN_PASSWORD_DICT)
def test_valid_users(login, password):
    assert utils.login_user(data.BASE_URL+data.USER_LOGIN, login, password) == ['token']

# PUT


