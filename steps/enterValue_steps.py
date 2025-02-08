from behave import *

@given("I am on the homepage and I click on the EnterSomeValue button")
def step_impl(context):
    context.enterValue_page.clickEnterValueButton()

@when("I fill the text '{text}'")
def step_impl(context, text):
    context.enterValue_page.enterValue(text)

@when("I click on the submit button")
def step_impl(context):
    context.enterValue_page.clickSubmitButton()

@then("I check if the text submitted appears on the page")
def step_impl(context):
    context.enterValue_page.verifyTextDisplay()