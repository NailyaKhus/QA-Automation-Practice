from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
waiting_time = 4

def Page_Loaded_Check_Out(base_url):
    driver.get(base_url)
    try:
        ele = WebDriverWait(driver, waiting_time).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Help')]")) )
        print("Page is loaded")
        flag = 1
    except:
        print(f"Timeout Exception: Page did not load within {waiting_time} seconds.")
        flag = 0
    return flag

def label_of_title_page(base_url):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.get(base_url)
        area = driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']")
        aria_label = area.get_attribute("aria-label")
        print('aria_label', aria_label)
        sleep(waiting_time)
        return aria_label
    else:
        return 'Timeout Exception: Page did not load'

def item_searching(base_url, item):
    flag = Page_Loaded_Check_Out(base_url)
    if flag == 1:
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(item)
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        sleep(waiting_time)
        item_space = driver.find_elements(By.XPATH, "//div[@data-asin]")
        item_space[2].click()
        sleep(waiting_time)
        title_text = driver.find_element(By.XPATH, "//h1[@id='title']").text
        return title_text.lower()
    else:
        return 'Timeout Exception: Page did not load'

def img_on_item_page(base_url, item):
    item_searching(base_url, item)
    item_image = driver.find_element(By.XPATH, "//div[@id='imgTagWrapperId']//img").get_attribute('src')
    driver.get(item_image)
    try:
        driver.find_element(By.XPATH, "//img")
        item_found = 1
    except:
        item_found = 0
    return item_found

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

