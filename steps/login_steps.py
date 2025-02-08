from behave import *

@given("I am on the homepage and I click on the LogIn button")
def step_impl(context):
    context.login_page.clickLoginButton()

@when("I enter the username '{email_text}' and the password '{pass_text}'")
def step_impl(context, email_text, pass_text):
    context.login_page.enterEmail(email_text)
    context.login_page.enterPassword(pass_text)

@when("I click on the login button")
def step_impl(context):
    context.login_page.clickOnLoginButton()

@when("the admin page appears")
def step_impl(context):
    context.login_page.verifyAdminScreen()

@when("I enter the text '{text_message}'")
def step_impl(context, text_message):
    context.login_page.enterText(text_message)

@then("I click on the Submit button")
def step_impl(context):
    context.login_page.clickOnSubmit()