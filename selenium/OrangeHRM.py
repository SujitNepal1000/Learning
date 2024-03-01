import time
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
driver = Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)

username = "//input[@name='username']"
password = "//input[@name='password']"
login = "//button[@type='submit']"
Dashboard = "//h6[text()='Dashboard']"

username_input_field = driver.find_element(By.XPATH, username)
username_input_field.send_keys("Admin")

password_input_field = driver.find_element(By.XPATH, password)
password_input_field.send_keys("admin123")

login_button = driver.find_element(By.XPATH, login)
login_button.click()

time.sleep(5)

login_succ = driver.find_element(By.XPATH, Dashboard)
assert login_succ.is_displayed()

time.sleep(5)
