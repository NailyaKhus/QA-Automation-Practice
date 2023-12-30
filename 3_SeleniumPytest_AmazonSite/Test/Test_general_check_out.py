import utils
import data

item = 'socks'
item_index = 1

def test_page_loaded():
    assert utils.Page_Loaded_Check_Out(data._base_url) == 1

def test_main_page_title():
    assert utils.label_of_title_page(data._base_url) == 'Amazon'

def test_item_name_in_title():
    title_text, _ = utils.item_title_and_img(data._base_url,item,item_index)
    assert item in title_text

def test_item_image_is_callable():
    _, img_is_callable = utils.item_title_and_img(data._base_url, item, item_index)
    assert img_is_callable == 1

def test_one_item_is_added():
    item_num_in_cart, _, _ = utils.press_add_to_cart(data._base_url,item,item_index)
    assert item_num_in_cart == 1

def test_ID_of_added_to_cart():
    _, added_item_id, in_cart_item_id = utils.press_add_to_cart(data._base_url,item,item_index)
    assert added_item_id == in_cart_item_id







