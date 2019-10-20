from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/farmazonne/Desktop/PythonCourse/chromedriver")
driver.get("https://accounts.google.com/")
driver.implicitly_wait(10)


first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
confirm_field = driver.find_element_by_name("ConfirmPasswd")
username_field = driver.find_element_by_id("username")

#controls
search_field = driver.find_element_by_id('searchInput')
search_button = driver.find_element_by_xpath('//button[@type = "submit"]')

#actions
"""Basic action on page"""
search_field.send_keys('Test Automation')
search_button.click()

#check
assert 'Test automation' in driver.title
assert 'Test automation ' in driver.title

#afterAll
driver.quit()
