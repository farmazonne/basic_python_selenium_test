from behave import *

from features.pages.login_page import LoginPage


@given("open login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given open login page')


@when('I type "{username}" in username field')
def step_impl(context, username):
    login_page = LoginPage(context.driver)
    login_page.enter_username(username)
    

@when('I type "pass" in password field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I type "pass" in password field')


@when("I click login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I click login button')


@then('I see "text" text')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I see "text" text')