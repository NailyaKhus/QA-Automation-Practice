import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def test_wrong_email_negativ_test():
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #driver = webdriver.Chrome()#(options=options)
    #driver.set_page_load_timeout(10)
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/")
    time.sleep(1)
    search_bar = driver.find_element(By.ID, 'nav-link-accountList').click()

    driver.find_element(By.ID, "ap_email").send_keys('jh@test.com')
    driver.find_element(By.ID, "continue").click()
    actual_value_alert_heading = driver.find_element(By.ID, "auth-error-message-box").\
        find_element(By.CLASS_NAME, "a-alert-heading").text
    expected_value_alert_heading = "There was a problem"

    assert expected_value_alert_heading == actual_value_alert_heading
    # search_bar.send_keys("Hello")#.send_keys(Keys.ENTER)
    # search_bar.send_keys(Keys.ENTER)
    #.click()

    #time.sleep(4)
    driver.quit()


