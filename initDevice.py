import yaml
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appiumServer import *

class initDevice():
    desired_caps = {}
    #Init device config
    def __init__(self, projectName, serial):
        file = open(projectName, 'r')
        data = yaml.load(file)
        desired = data.get(serial)
        self.desired_caps['platformName'] = desired['platformName']
        self.desired_caps['platformVersion'] = desired['platformVersion']
        self.desired_caps['deviceName'] = desired['deviceName']
        self.desired_caps['app'] = desired['app']
        self.desired_caps['appActivity'] = desired['appActivity']
        self.desired_caps['appPackage'] = desired['appPackage']
        self.desired_caps['udid'] = desired['udid']
        self.port= desired['port']
        self.desired_caps['automationName'] = 'Uiautomator2' #for get toast info
        #desired_caps['unicodeKeyboard'] = True
        #desired_caps['resetKeyboard'] = True
        self.s = AppiumServer()
        self.s.start_appium('127.0.0.1', self.port)
        time.sleep(3)

    def getDeriver(self):
        self.driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(self.port), self.desired_caps)
        appium_server_url = 'http://127.0.0.1:{}/wd/hub'.format(self.port)
        print('Connect {} successful!'.format(appium_server_url))
        return self.driver

    def getPort(self):
        return self.port

    def getAppiumServer(self):
        return self.s





