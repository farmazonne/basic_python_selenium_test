import configparser

from selenium import webdriver


def before_all(context):
    parser = configparser.ConfigParser()
    parser.read('./features/config/behave.ini')
    context.config = parser

    context.driver = webdriver.Chrome("C:/Users/farmazonne/Desktop/PythonCourse/chromedriver")
    context.driver.implicitly_wait(10)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_all(context):
    context.driver.quit()
