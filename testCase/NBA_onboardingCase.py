#-*- encoding = utf-8 -*-
import unittest
from initDevice import *
from ParametrizedCase import *
from appiumServer import killport
from threading import Lock
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from myFindElement import MyFindElement
lock = Lock()




class testCase(ParametrizedTestCase):

    def setUp(self):
        lock.acquire()
        self.device = initDevice('projectDeviceConfig\\nbaConfig.yaml',self.param)
        self.driver = self.device.getDeriver()
        lock.release()
        self.myDriver = MyFindElement(self.driver, "elementsConfig\\nba.yaml")
        try:
            self.myDriver.findElement("id","qaConfig").click()
        except Exception:
            print("Config is not qa!")
            pass

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        # port = self.device.getPort()
        # killport(port)
        # time.sleep(3)


    @unittest.skip("not need")
    def test_onboarding_DL(self):
        for i in range(3):
            for i in range(2):
                location = self.myDriver.findElement("id","DL").location
                size = self.myDriver.findElement("id","DL").size
                x = location['x']
                y = location['y']
                width = size['width']
                self.driver.swipe(x + width * 0.8, y, x, y, 500 )
                time.sleep(2)
            for i in range(2):
                location = self.myDriver.findElement("id", "DL").location
                size = self.myDriver.findElement("id","DL").size
                x = location['x']
                y = location['y']
                width = size['width']
                height = size['height']
                self.driver.swipe(x, y, x + width * 0.8, y, 500)
                time.sleep(2)

    @unittest.skip("not need")
    def test_myFavoriteTeam(self):
        #login an account
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(
            "eloy0831@qq.com")
        self.myDriver.findElement("id", "passwordBox").send_keys("111111")
        self.myDriver.findElement("id", "siginButton").click()
        #Enter to my favorite team page, remove my fav team
        try:
            while True:
                self.myDriver.findElement("xpath","myFavTeam").click()
                print("Remove a team successfully!")
        except Exception:
            errorMsg = self.myDriver.findElement("id","myFavTeamText").text
            print(errorMsg)

        #add my fav team
        for i in range(6):
            self.myDriver.findElement("xpath", "favTeam").click()
            print("Add a team successfully!")
        self.myDriver.is_toast_exist("maxFavTeam")
        self.myDriver.findElement("id","skipButton").click()

    #@unittest.skip("no need")
    def test_notifications(self):
        # login an account
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(
            "eloy0831@qq.com")
        self.myDriver.findElement("id", "passwordBox").send_keys("111111")
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")
        # enter to notification page
        self.myDriver.findElement("id", "continueButton").click()
        self.myDriver.findElement("id", "allow").click()
        elements = self.myDriver.findElements("id", "notificationSwitch")
        for i in range(len(elements)):
            elements[i].click()
        location = self.myDriver.findElement("id", "notificationRoll").location
        size = self.myDriver.findElement("id", "notificationRoll").size
        self.driver.swipe(location['x']+size['width']/2,location['y'] + size['height']*0.8\
                ,location['x']+size['width']/2, location['y'], 500)
        elements = self.myDriver.findElements("id", "notificationSwitch")
        for i in range(len(elements)):
            elements[i].click()
        self.myDriver.findElement("id", "continueButton").click()




