from selenium import webdriver

driver = webdriver.Chrome("C:/Users/farmazonne/Desktop/PythonCourse/chromedriver")
driver.get("https://www.wikipedia.org/")

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
