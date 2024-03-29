import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@when('I click element with text "{text}"')
def step_impl(context, text):
    element = (By.XPATH, "//*[text() = '{}']".format(text))
    WebDriverWait(context.driver, 5).until(ec.presence_of_element_located(element))
    WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable(element), "Unable to click element").click()


@then('I see element with text "{text}"')
def step_impl(context, text):
    element = (By.TAG_NAME, "body")
    WebDriverWait(context.driver, 10).until(ec.text_to_be_present_in_element(element, text), "Unable to find text")