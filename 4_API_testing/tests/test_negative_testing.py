import utils
import data
import pytest
import requests

@pytest.mark.parametrize("uri", data.INCORRECT_PRODUCT_URI_LIST)
def test_invalid_product_url(uri):
    with pytest.raises(requests.exceptions.JSONDecodeError):
        utils.response_get(data.BASE_URL + "/products/" + uri).json()

@pytest.mark.parametrize("body", data.INCORRECT_PRODUCT_BODY_LIST)
def test_invalid_product_body(body):
    assert str(utils.request_post(data.BASE_URL + data.URI_PRODUCT_PATH, body)) == '<Response [404]>'


