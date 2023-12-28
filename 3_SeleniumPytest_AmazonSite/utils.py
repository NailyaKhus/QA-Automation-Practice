from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
waiting_time = 4

# Did the Main page load
def Page_Loaded_Check_Out(base_url):
    driver.get(base_url)
    try:
        WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Help')]")) )
        print("Page is loaded")
        flag = 1
    except:
        print(f"Timeout Exception: Page did not load within {waiting_time} seconds.")
        flag = 0
    return flag

# Is the label of the Main page "Amazon"
def label_of_title_page(base_url):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.get(base_url)
        area = driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']")
        aria_label = area.get_attribute("aria-label")
        sleep(waiting_time)
        return aria_label
    else:
        return 'Timeout Exception: Page did not load'

#
def item_searching(base_url, item, item_index):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(item)
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        sleep(waiting_time)
        item_space = driver.find_elements(By.XPATH, "//div[@data-asin]")
        item_space[item_index].click()
        sleep(waiting_time)
        return driver
    else:
        return 'Timeout Exception: Page did not load'

# Does the title of the item contain searched word
# Is the image of the item callable
def item_title_and_img(base_url, item, item_index):
    driver = item_searching(base_url, item, item_index)
    title_text = driver.find_element(By.XPATH, "//h1[@id='title']").text
    item_image = driver.find_element(By.XPATH, "//div[@id='imgTagWrapperId']//img").get_attribute('src')
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
        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()

    # If pressing to "Add to cart" failed, choose next item on the item-searching page
    except:
        item_index+=1
        driver = item_searching(base_url, item, item_index)
        item_url = driver.current_url
        item_url = item_url.split('/')
        # Saving the item's id to check it in the Cart
        added_item_id = item_url[item_url.index('dp') + 1]
        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()

    # Go to the Cart page
    driver.find_element(By.XPATH, "//a[@id='nav-cart']//span[contains(text(),'Cart')]").click()
    # Saving number of items in the cart
    item_num_in_cart = driver.find_element(By.XPATH,"//div[@data-name='Subtotals']//span[contains(text(),'Subtotal')]").text
    item_num_in_cart = item_num_in_cart.replace('(', '').split(' ')
    item_num_in_cart = int(item_num_in_cart[1])
    in_cart_item_id = driver.find_element(By.XPATH, "//div[@data-name='Active Items']//div[@data-itemtype='active']").get_attribute('data-asin')
    # Cart Cleaning
    driver.find_element(By.XPATH, "//div[@data-name='Active Items']//span[@data-action='delete']").click()
    return item_num_in_cart, added_item_id, in_cart_item_id

# Loading the sign-in page and entering login to the input box
def load_sign_in_page(base_url, login):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.find_element(By.XPATH, "//span[text()='Hello, sign in']").click()
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        sleep(waiting_time)
        actual_value_alert_heading = driver.find_element(By.CLASS_NAME, "a-alert-heading").text
        return actual_value_alert_heading
    else:
        return 'Timeout Exception: Page did not load'

