from behave import *

@given("I am on the basepage and I click on the ScrollView button and I assert that after click I am on the right page")
def step_impl(context):
    context.scrollView_page.clickScrollViewButton()

@when("I scroll to button 16 and I make sure the button is visible")
def step_impl(context):
    context.scrollView_page.scrollToButton()

@when("I click on button 16")
def step_impl(context):
    context.scrollView_page.clickScrolledButton()

@then("a pop-up appears and I press Yes")
def step_impl(context):
    context.scrollView_page.clickPopMessage()