from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from traceback import print_stack


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait =WebDriverWait(self.driver, 25, poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotVisibleException, NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == 'class':
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == 'des':
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % locatorValue))
            return element
        elif locatorType == 'index':
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().index("%d")' % int(locatorValue)))
            return element
        elif locatorType == 'text':
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorValue))
            return element
        elif locatorType == 'scroll':
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(text("%s"))' % locatorValue))
            return element
        elif locatorType == 'xpath':
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locatorValue))
            return element

        return element

    def getElement(self,locatorValue,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
        except:
            print("Element not found with LocatorType: " + locatorType + " with the locatorValue:" + locatorValue)
            print_stack()
        return element

    def clickElement(self,locatorValue,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
        except:
            print("Unable to click element with LocatorType: " + locatorType + " with the locatorValue: " + locatorValue)
            print_stack()


    def sendText(self,text,locatorValue,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
        except:
            print("Unable to send text on element with LocatorType: " + locatorType + " with the locatorValue: " + locatorValue)
            print_stack()

    def isDiplayed(self,locatorValue,locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            return True
        except:
            print("Element with LocatorType: " + locatorType + " with the locatorValue: " + locatorValue+" is not displayed")
            print_stack()
            return False

    def getText(self,locatorValue,locatorType='id'):
        elementText = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementText = webElement.text
            return True
        except:
            print("No text found for element with LocatorType: " + locatorType + " with the locatorValue: " + locatorValue)
            print_stack()
        return elementText



