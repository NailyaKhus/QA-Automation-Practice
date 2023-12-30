import pytest
import utils
import data

# invalid emails
@pytest.mark.parametrize("email", ['jh@test.com', 'test.com', 'test@test@test.com', 'test@.com', '@test.com', 'test!test@test.com', '75@754396', '866_754343673', '754A634569'])
def test_invalid_email(email):
    assert utils.load_sign_in_page(data._base_url, email) == data.THERE_WAS_A_PROBLEM

# invalid phone numbers
@pytest.mark.parametrize("phone", ['000', '22 22983', '8664382668408'])
def test_invalid_phone_number(phone):
    assert utils.load_sign_in_page(data._base_url, phone) == data.INCORRECT_PHONE_NUMBER