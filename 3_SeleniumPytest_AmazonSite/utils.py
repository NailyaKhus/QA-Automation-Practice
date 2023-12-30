from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import data

driver = webdriver.Chrome()
waiting_time = 4

# selectors
HELP = "//a[contains(text(),'Help')]"
LABEL = "//a[@id='nav-logo-sprites']"
ITEM_SEARCH_BAR = "//input[@type='text']"
GO_BUTTON = "//input[@value='Go']"
ITEMS = "//div[@data-asin]"
ITEM_TITLE = "//h1[@id='title']"
ITEM_IMAGE = "//div[@id='imgTagWrapperId']//img"
ADD_TO_CART_BUTTON = "//input[@id='add-to-cart-button']"
CART_BUTTON = "//a[@id='nav-cart']//span[contains(text(),'Cart')]"
SUBTOTALS_IN_THE_CART = "//div[@data-name='Subtotals']//span[contains(text(),'Subtotal')]"
ID_OF_ITEM_IN_CART = "//div[@data-name='Active Items']//div[@data-itemtype='active']"
DELETE_FROM_CART_BUTTON = "//div[@data-name='Active Items']//span[@data-action='delete']"
SIGN_IN_BUTTON = "//span[text()='Hello, sign in']"
EMAIL_OR_PHONE_INPUT_PANEL = "//input[@type='email']"
SIGN_IN_CONTINUE_BUTTON = "//input[@id='continue']"
SIGN_IN_ALERT = "a-alert-heading"

# Did the Main page load
def Page_Loaded_Check_Out(base_url):
    driver.get(base_url)
    try:
        WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.XPATH, HELP)) )
        print("Page is loaded")
        flag = 1
    except:
        print(data.TIMEOUT_EXCEPTION_PAGE_DID_NOT_LOAD)
        flag = 0
    return flag

# Is the label of the Main page "Amazon"
def label_of_title_page(base_url):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.get(base_url)
        area = driver.find_element(By.XPATH, LABEL)
        aria_label = area.get_attribute("aria-label")
        sleep(waiting_time)
        return aria_label
    else:
        return data.TIMEOUT_EXCEPTION_PAGE_DID_NOT_LOAD

def item_searching(base_url, item, item_index):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.find_element(By.XPATH, ITEM_SEARCH_BAR).send_keys(item)
        driver.find_element(By.XPATH, GO_BUTTON).click()
        sleep(waiting_time)
        item_space = driver.find_elements(By.XPATH, ITEMS)
        item_space[item_index].click()
        sleep(waiting_time)
        return driver
    else:
        return data.TIMEOUT_EXCEPTION_PAGE_DID_NOT_LOAD

# Does the title of the item contain searched word
# Is the image of the item callable
def item_title_and_img(base_url, item, item_index):
    driver = item_searching(base_url, item, item_index)
    title_text = driver.find_element(By.XPATH, ITEM_TITLE).text
    item_image = driver.find_element(By.XPATH, ITEM_IMAGE).get_attribute('src')
    driver.get(item_image)
    sleep(waiting_time)
    try:
        driver.find_element(By.XPATH, "//img")
        item_is_callable = 1
    except:
        item_is_callable = 0
    return title_text.lower(), item_is_callable

# Add to cart
def press_add_to_cart(base_url, item, item_index):
    # Saving item's id and pressing to the button "Add to cart"
    try:
        driver = item_searching(base_url, item, item_index)
        item_url = driver.current_url
        item_url = item_url.split('/')
        # Saving the item's id to check it in the Cart
        added_item_id = item_url[item_url.index('dp') + 1]
        driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).click()

    # If pressing to "Add to cart" failed, choose next item on the item-searching page
    except:
        item_index+=1
        driver = item_searching(base_url, item, item_index)
        item_url = driver.current_url
        item_url = item_url.split('/')
        # Saving the item's id to check it in the Cart
        added_item_id = item_url[item_url.index('dp') + 1]
        driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).click()

    # Go to the Cart page
    driver.find_element(By.XPATH, CART_BUTTON).click()
    # Saving number of items in the cart
    item_num_in_cart = driver.find_element(By.XPATH, SUBTOTALS_IN_THE_CART).text
    item_num_in_cart = item_num_in_cart.replace('(', '').split(' ')
    item_num_in_cart = int(item_num_in_cart[1])
    in_cart_item_id = driver.find_element(By.XPATH, ID_OF_ITEM_IN_CART).get_attribute('data-asin')
    # Cart Cleaning
    driver.find_element(By.XPATH, DELETE_FROM_CART_BUTTON).click()
    return item_num_in_cart, added_item_id, in_cart_item_id

# Loading the sign-in page and entering login to the input box
def load_sign_in_page(base_url, login):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.find_element(By.XPATH, SIGN_IN_BUTTON).click()
        driver.find_element(By.XPATH, EMAIL_OR_PHONE_INPUT_PANEL).send_keys(login)
        driver.find_element(By.XPATH, SIGN_IN_CONTINUE_BUTTON).click()
        sleep(waiting_time)
        actual_value_alert_heading = driver.find_element(By.CLASS_NAME, SIGN_IN_ALERT).text
        return actual_value_alert_heading
    else:
        return data.TIMEOUT_EXCEPTION_PAGE_DID_NOT_LOAD

