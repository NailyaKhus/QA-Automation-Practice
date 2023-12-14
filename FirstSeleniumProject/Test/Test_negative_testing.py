import pytest
import utils

_base_url = "https://www.amazon.com/"
THERE_WAS_A_PROBLEM = 'There was a problem'
INCORRECT_PHONE_NUMBER = 'Incorrect phone number'

@pytest.mark.parametrize("email", ['jh@test.com', 'test.com', 'test@test@test.com', 'test@.com', '@test.com', 'test!test@test.com', '75@754396', '866_754343673', '754A634569'])
def test_wrong_email(email):
    assert utils.load_sign_in_page(_base_url, email) == THERE_WAS_A_PROBLEM


@pytest.mark.parametrize("email", ['000', '22 22983', '8664382668408'])
def test_wrong_phone_number(email):
    assert utils.load_sign_in_page(_base_url, email) == INCORRECT_PHONE_NUMBER