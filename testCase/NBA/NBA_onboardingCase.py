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
from ddt import ddt,data,unpack
lock = Lock()



@ddt
class testSuit_onboarding_UI(ParametrizedTestCase):

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
        pass


    # @unittest.skip("not need")
    def test_onboarding_DL(self):
        for i in range(3):
            for i in range(2):
                location = self.myDriver.findElement_location("id","DL")
                x = location['x']
                y = location['y']
                width = location['width']
                self.driver.swipe(x + width * 0.8, y, x, y, 500 )
                time.sleep(2)
            for i in range(2):
                location = self.myDriver.findElement_location("id", "DL")
                x = location['x']
                y = location['y']
                width = location['width']
                self.driver.swipe(x, y, x + width * 0.8, y, 500)
                time.sleep(2)

    # @unittest.skip("not need")
    @data(["eloy0831@qq.com", "111111"])
    @unpack
    def test_onboarding_myFavoriteTeam(self, user, psw):
        #login an account
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        #Enter to my favorite team page, remove my fav team
        try:
            counter = 0
            while True:
                self.myDriver.findElement("xpath","favTeam").click()
                counter += 1
                # print("Remove a team successfully!")
        except Exception as eMsg:
            errorMsg = self.myDriver.findElement("id","myFavTeamText").text
            msgRef = "No content is available at this time. Please check back later."
            msgRef_ = "You currently have no \"Favorite\" teams.  Tap a team to \"Favorite\"."
            if counter > 0:
                self.assertEqual(errorMsg, msgRef_, msg="Error Message is worng!")
            else:
                self.assertEqual(errorMsg, msgRef, msg="Error Message is worng!")
        #add my fav team
        for i in range(6):
            self.myDriver.findElement("xpath", "team").click()
            # print("Add a team successfully!")
        self.myDriver.is_toast_exist("maxFavTeam")


    # @unittest.skip("no need")
    @data(["eloy0831@qq.com", "111111"])
    @unpack
    def test_onboarding_notifications(self, user, psw):
        # login an account
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")
        # enter to notification page
        self.myDriver.findElement("id", "continueButton").click()
        self.myDriver.findElement("id", "allow").click()
        elements = self.myDriver.findElements("id", "notificationSwitch")
        for i in range(len(elements)):
            elements[i].click()
        location = self.myDriver.findElement_location("id", "notificationRoll")
        self.driver.swipe(location['x']+location['width']/2,location['y'] + location['height']*0.8\
                ,location['x']+location['width']/2, location['y'], 500)
        elements = self.myDriver.findElements("id", "notificationSwitch")
        for i in range(len(elements)):
            elements[i].click()
        self.myDriver.findElement("id", "continueButton").click()




