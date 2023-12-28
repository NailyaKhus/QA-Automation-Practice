import utils

_base_url = "https://www.amazon.com/"
item = 'socks'
item_index = 1

# checking test for the Main page
def test_page_loaded():
    assert utils.Page_Loaded_Check_Out(_base_url) == 1 # page is loded or not
    assert utils.label_of_title_page(_base_url) == 'Amazon' # the text in the title label is "Amazon"

# cheching products
# searching the product
def test_item_name_in_title():
    title_text, img_is_callable = utils.item_title_and_img(_base_url,item,item_index)
    assert item in title_text
    assert img_is_callable == 1

# Add to cart
def test_add_to_cart():
    item_num_in_cart, added_item_id, in_cart_item_id = utils.press_add_to_cart(_base_url,item,item_index)
    assert item_num_in_cart == 1
    assert added_item_id == in_cart_item_id







