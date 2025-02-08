from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import AppiumOptions

class Driver:

    def __init__(self):
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            appium_service = AppiumService()
            appium_service.start()

            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['automationName'] = 'UiAutomator2'
            desired_caps['platformVersion'] = '13'
            desired_caps['deviceName'] = 'samsung SM-G988B'
            desired_caps['app'] = (r"C:/Users/User/Documents/Code2Lead/Others/Android_Appium_Demo.apk")
            desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
            desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

            appium_options = AppiumOptions()
            appium_options.load_capabilities(desired_caps)

            self.driver = webdriver.Remote("http://127.0.0.1:4723", options=appium_options)

        return self.driver

