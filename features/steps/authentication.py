from behave import *
from selenium import webdriver



@given("I am on the login page")
def step_impl(context):
    context.browser.get(context.base_url + '/login/')
    

@when("I enter valid admin credentials")
def step_impl(context):
   # Find the username and password fields and enter valid admin credentials
    context.browser.find_element_by_id('email').send_keys('admin')
    context.browser.find_element_by_id('password').send_keys('adminS')


@when("I enter valid normal user credentials")
def step_impl(context):
    # Implement code to enter valid normal user credentials
    pass

@when("click the login button")
def step_impl(context):
    # Implement code to click the login button
    pass

@when("I am logged in")
def step_impl(context):
    # Implement code to log in
    pass

@when("click the logout button")
def step_impl(context):
    # Implement code to click the logout button
    pass

@then("I should be redirected to the admin dashboard")
def step_impl(context):
    # Implement code to check if redirected to admin dashboard
    pass

@then("I should be redirected to the vehicle list page")
def step_impl(context):
    # Implement code to check if redirected to vehicle list page
    pass

@then("I should be redirected to the login page")
def step_impl(context):
    # Implement code to check if redirected to login page
    pass