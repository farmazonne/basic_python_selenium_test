from selenium import webdriver
from pages.sign_in_page import SignIn
from pages.create_account_page import CreateAccount

driver = webdriver.Chrome("C:/Users/farmazonne/Desktop/PythonCourse/chromedriver")
driver.get("https://accounts.google.com/")
driver.implicitly_wait(10)

data = {'name': 'Ahalai', 'lastname': 'Mahalai', 'password': 'Qwerty12345!'}
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a', 'a@-a.a', '@a.a'}
error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."

sign_in_page = SignIn(driver)
sign_in_page.create_new_account()

create_account_page = CreateAccount(driver)
create_account_page.fill_data(data)

for email in email_list:
    create_account_page.validate_email(email, error)

driver.quit()



