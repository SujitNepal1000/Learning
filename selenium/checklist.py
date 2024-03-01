import time
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
driver = Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")

check_link = "//ul/li/a[text()='Checkboxes']"
checkbox_1 = "//form[@id='checkboxes']/input[1]"
checkbox_2 = "//form[@id='checkboxes']/input[2]"

check_button = driver.find_element(By.XPATH, check_link)
check_button.click()

checkbox_one = driver.find_element(By.XPATH, checkbox_1)
checkbox_one.click()

checkbox_two = driver.find_element(By.XPATH, checkbox_2)
checkbox_two.click()

time.sleep(2)
