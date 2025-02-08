import time

from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _loginButton = "com.skill2lead.appiumdemo:id/Login"  # id
    _enterEmail = "com.skill2lead.appiumdemo:id/Et4"  # id
    _enterPassword = "Enter Password"  # text
    _clickSubmitButton = "com.skill2lead.appiumdemo:id/Btn3"  # id
    _pageTextEnterAdmin = "Enter Admin"  # text
    _enterTextEnterAdmin = "com.skill2lead.appiumdemo:id/Edt_admin"  # id
    _clickSubmitButtonAdmin = "com.skill2lead.appiumdemo:id/Btn_admin_sub"  # id

    def clickLoginButton(self):
        self.clickElement(self._loginButton, 'id')

    def enterEmail(self,email_text):
        self.sendText(email_text, self._enterEmail, 'id')

    def enterPassword(self, pass_text):
        self.sendText(pass_text, self._enterPassword, 'text')

    def clickOnLoginButton(self):
        self.clickElement(self._clickSubmitButton, 'id')

    def verifyAdminScreen(self):
        adminScreen = self.isDiplayed(self._pageTextEnterAdmin, 'text')
        assert adminScreen == True

    def enterText(self, text_message):
        self.sendText(text_message, self._enterTextEnterAdmin, 'id')

    def clickOnSubmit(self):
        self.clickElement(self._clickSubmitButtonAdmin, 'id')

    def close_driver(self):
        time.sleep(5)
        self.driver.quit()
