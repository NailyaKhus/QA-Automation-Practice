import utils

_base_url = "https://www.amazon.com/"
item = 'socks'

# checking test for the Main page
def test_page_loaded():
    assert utils.Page_Loaded_Check_Out(_base_url) == 1 # page is loded or not
    assert utils.label_of_title_page(_base_url) == 'Amazon' # the text in the title label is "Amazon"

# cheching products
# searching the product
def test_item_name_in_title():
    assert item in utils.item_searching(_base_url,item)

# image is on the page of item
def test_active_img_on_item_page():
    assert utils.img_on_item_page(_base_url,item) == 1






