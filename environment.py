from app_browser import Driver
from pages.enterValue_page import EnterValuePage
from pages.login_page import LoginPage
from pages.scrollView_page import ScrollViewPage


def before_scenario(context, scenario):
    context.driver = Driver().get_driver()
    context.login_page = LoginPage(context.driver)
    context.enterValue_page = EnterValuePage(context.driver)
    context.scrollView_page = ScrollViewPage(context.driver)

def after_scenario(context, scenario):
    context.login_page.close_driver()