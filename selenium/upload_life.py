import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
file_link = "//ul/li/a[text()='File Upload']"
choose_file = "file-upload"
file_upload = "//input[@id='file-submit']"

check_btn = driver.find_element(By.XPATH, file_link)
check_btn.click()

time.sleep(5)

choose_btn = driver.find_element(By.ID, choose_file)
choose_btn.send_key("C://Users//HP//Desktop//test.txt")
time.sleep(3)

upload_btn = driver.find_element(By.XPATH, file_upload)
upload_btn.click()

time.sleep(5)
