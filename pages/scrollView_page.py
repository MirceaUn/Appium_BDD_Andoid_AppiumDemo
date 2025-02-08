from pages.base_page import BasePage

class ScrollViewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _scrollViewButton = "com.skill2lead.appiumdemo:id/ScrollView" #id
    _titleScrollView = "ScrollView" #text
    _button16 = "BUTTON16" #scroll
    _popUpYesButton = "android:id/button1" #id

    def clickScrollViewButton(self):
        self.clickElement(self._scrollViewButton, 'id')
        assert self.isDiplayed(self._titleScrollView, 'text')

    def scrollToButton(self):
        self.getElement(self._button16, 'scroll')
        assert self.isDiplayed(self._button16, 'scroll')

    def clickScrolledButton(self):
        self.clickElement(self._button16, 'scroll')

    def clickPopMessage(self):
        self.clickElement(self._popUpYesButton, 'id')

