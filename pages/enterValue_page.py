from pages.base_page import BasePage

class EnterValuePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _enterValueButton = "com.skill2lead.appiumdemo:id/EnterValue" # id
    _pageTextEnterValue = "Enter some Value" #text
    _enterValueField = "com.skill2lead.appiumdemo:id/Et1" #id
    _submitButton = "com.skill2lead.appiumdemo:id/Btn1" #id
    _previewField = "com.skill2lead.appiumdemo:id/Tv1" #id

    def clickEnterValueButton(self):
        self.clickElement(self._enterValueButton, 'id')
        assert self.isDiplayed(self._pageTextEnterValue, 'text')

    def enterValue(self, text):
        self.sendText(text, self._enterValueField, 'id')

    def clickSubmitButton(self):
        self.clickElement(self._submitButton, 'id')

    def verifyTextDisplay(self):
        text = self.getText(self._enterValueField, 'id')
        text_displayed = self.getText(self._previewField, 'id')
        assert text == text_displayed
