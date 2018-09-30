#-*- encoding = utf-8 -*-
import unittest
import time
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
class testSuit_MyAccount_videosTap(ParametrizedTestCase):

    def setUp(self):
        lock.acquire()
        self.device = initDevice('projectDeviceConfig\\nbaConfig.yaml',self.param)
        self.driver = self.device.getDeriver()
        lock.release()
        self.myDriver = MyFindElement(self.driver,"elementsConfig\\nba.yaml")
        try:
            self.myDriver.findElement("id","qaConfig").click()
        except Exception:
            print("Config is not qa!")
        self.myDriver.findElement("id", "skipButton").click()
        try:
            self.myDriver.findElement("id", "sysButton2").click()
        except Exception:
            print("Device has google service!")
        self.myDriver.findElement("id", "enterMyAccount").click()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass

    # @unittest.skip("not need")
    @data(["eloy0831@qq.com","111111"])
    @unpack
    def test_videosTap_videoOperation(self, user, psw):
        self.myDriver.findElement("id", "myFavorites").click()
        self.myDriver.findElement("id", "favSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")
        # self.myDriver.findElement("xpath", "favVideoStar").click()
        self.myDriver.findElement("xpath", "favVideoShare").click()
        time.sleep(2)
        self.driver.keyevent(4)
        for i in range(2):
            location = self.myDriver.findElement_location("id", "favVideoList")
            x = location["x"]
            y = location["y"]
            h = location["height"]
            w = location["width"]
            self.driver.swipe(x + w/2, y + h*0.8, x + w/2, y, 3000)
        items = self.myDriver.findElements("className", "favVideos")
        items[0].click()
        time.sleep(10)
        self.myDriver.screenshot()

@ddt
class testSuit_MyAccount_teamsTap(ParametrizedTestCase):

    def setUp(self):
        lock.acquire()
        self.device = initDevice('projectDeviceConfig\\nbaConfig.yaml', self.param)
        self.driver = self.device.getDeriver()
        lock.release()
        self.myDriver = MyFindElement(self.driver, "elementsConfig\\nba.yaml")
        try:
            self.myDriver.findElement("id", "qaConfig").click()
        except Exception:
            print("Config is not qa!")
        self.myDriver.findElement("id", "skipButton").click()
        try:
            self.myDriver.findElement("id", "sysButton2").click()
        except Exception:
            print("Device has google service!")
        self.myDriver.findElement("id", "enterMyAccount").click()
        self.myDriver.findElement("id", "myFavorites").click()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass

    # @unittest.skip("not need")
    @data(["eloy0831@qq.com","111111"])
    @unpack
    def test_teamsTap_addFavTeams(self, user, psw):
        self.myDriver.findElement("xpath", "teamsTap").click()
        self.myDriver.findElement("id", "favSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")
        for i in range(6):
            self.myDriver.findElement("xpath", "team").click()
        self.myDriver.is_toast_exist("maxFavTeam")

    # @unittest.skip("not need")
    @data(["eloy0831@qq.com", "111111"])
    @unpack
    def test_teamsTap_removeFavTeams(self, user, psw):
        self.myDriver.findElement("xpath", "teamsTap").click()
        self.myDriver.findElement("id", "favSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")
        location = self.myDriver.findElement_location("id", "favTeamList")
        x = location["x"]
        y = location["y"]
        h = location["height"]
        self.driver.swipe(x, y, x, y + h*0.7, 3000)
        try:
            for i in range(6):
                self.myDriver.findElement("xpath", "favTeam").click()
                # self.myDriver.is_toast_exist("")
        except Exception as msg:
            emsg = self.myDriver.findElement("id", "favTeamError").text
            emsgRefer = "You currently have no \"Favorite\" teams.  Tap a team to \"Favorite\"."
            self.assertEqual(emsg, emsgRefer, msg="Error messarge is worng!")
        for i in range(2):
            self.myDriver.findElement("xpath", "team").click()

@ddt
class testSuit_MyAccount_playersTap(ParametrizedTestCase):

    def setUp(self):
        lock.acquire()
        self.device = initDevice('projectDeviceConfig\\nbaConfig.yaml', self.param)
        self.driver = self.device.getDeriver()
        lock.release()
        self.myDriver = MyFindElement(self.driver, "elementsConfig\\nba.yaml")
        try:
            self.myDriver.findElement("id", "qaConfig").click()
        except Exception:
            print("Config is not qa!")
        self.myDriver.findElement("id", "skipButton").click()
        try:
            self.myDriver.findElement("id", "sysButton2").click()
        except Exception:
            print("Device has google service!")
        self.myDriver.findElement("id", "enterMyAccount").click()
        self.myDriver.findElement("id", "myFavorites").click()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass

    @data(["eloy0831@qq.com", "111111"])
    @unpack
    def test_playersTap_addPlayer(self, user, psw):
        self.myDriver.findElement("xpath", "playersTap").click()
        self.myDriver.findElement("id", "favSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")
        try:
            for i in range(3):
                self.myDriver.findElement("xpath", "player").click()
        except Exception as eMsg:
            errorMsg = self.myDriver.findElement("id", "favPlayerTeamError").text
            msgRef = "You currently have no \"Favorite\" teams.  Tap a team to \"Favorite\"."
            self.assertEqual(errorMsg, msgRef, msg="Error message is worng!" )
















