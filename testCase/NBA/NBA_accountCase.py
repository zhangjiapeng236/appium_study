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
class testSuit_Account_login(ParametrizedTestCase):

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

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass

    # @unittest.skip("not need")
    @data(["eloy0831@qq.com","111111"],[" eloy0916@qq.com ","111111"])
    @unpack
    def test_account_loginSuccessful(self, user, psw):
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

    # @unittest.skip("not need")
    @data(["eloy0131@qq.com", "111111"],["eloy0116@qq.com", "111111"])
    @unpack
    def test_account_loginNotFound(self, user, psw):
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginNotFound")

    # @unittest.skip("not need")
    @data(["eloy", "111111"],["eloy0116@qq.com", ""],["","11111"],["#$%^", "23"])
    @unpack
    def test_account_loginError(self, user, psw):
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        try:
            print(self.myDriver.findElement("id", "inputError").text)
        except Exception as errorMsg:
            print(errorMsg)

    # @unittest.skip("not need")
    @data(["eloy08311@qq.com"], ["eloy"], ["eloy0831@qq.com"], [""])
    @unpack
    def test_account_forgotPassword(self, user):
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "forgotPassword").click()
        self.myDriver.findElement("id", "forgotUsername").send_keys(user)
        self.myDriver.findElement("id", "sendButton").click()
        try:
            self.myDriver.is_toast_exist("resetFailed")
        except Exception as errorMsg:
            print(errorMsg)
        try:
            print(self.myDriver.findElement("id", "inputError").text)
        except Exception as errorMsg:
            print(errorMsg)
        try:
            self.myDriver.findElement("id", "resetSigin").click()
        except Exception as errorMsg:
            print(errorMsg)

@ddt
class testSuit_Account_regist(ParametrizedTestCase):
    user = "eloy" + time.strftime("%Y%m%d%H%M%S")+"@neuqa.com"
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

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass

    @data([user, "111111"])
    @unpack
    def test_account_registSuccessful(self, username, psw):
        self.myDriver.findElement("id", "getStarted").click()
        self.myDriver.findElement("id", "userBox").send_keys(username)
        self.myDriver.findElement("id", "registerPswBox").send_keys(psw)
        location = self.myDriver.findElement_location("id", "registerScorll")
        x = location["x"]
        y = location["y"]
        h = location["height"]
        self.driver.swipe(x, y + h*0.7, x, y, 2000)
        checkBox = self.myDriver.findElements("className", "checkBoxs")
        for i in range(3):
            checkBox[i].click()
        self.myDriver.findElement("id", "creatAccount").click()
        time.sleep(3)
        self.myDriver.is_toast_exist("creatAccountSuccess")







@ddt
class testSuit_Account_subscription(ParametrizedTestCase):

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

    @data(["eloy0831@qq.com", "111111"])
    @unpack
    def test_account_subscription(self, user, psw):
        self.myDriver.findElement("id", "menuSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")
        self.myDriver.findElement("id","myPackages").click()
        packageTitle = self.myDriver.findElement("xpath", "myPackagesTitle").text
        packageLabel = self.myDriver.findElement("id", "packageLabel").text
        packageName = self.myDriver.findElement("id", "packageName").text
        packageHistoryLable = self.myDriver.findElement("id", "packageHistoryLable").text
        packageDescripton = self.myDriver.findElement("id", "packageDescription").text
        purchaseDate = self.myDriver.findElement("id", "purchaseDate").text
        gameEvent = self.myDriver.findElement("xpath", "gameEvent").text
        gameDate = self.myDriver.findElement("xpath", "gameDate").text
        self.assertEqual(packageTitle, "My Packages", msg="Text is worng!")
        self.assertEqual(packageLabel, "My Subscriptions", msg="Text is worng!")
        self.assertEqual(packageName, "League Pass", msg="Text is worng!")
        self.assertEqual(packageHistoryLable, "My Games", msg="Text is woring!")
        self.assertEqual(packageDescripton, "Description", msg="Text is woring!")
        self.assertEqual(purchaseDate, "Purchase Date", msg="Text is worng!")
        self.assertEqual(gameEvent, "Hornetsa lasPistonsel 18-oct-2017", msg="Text is worng!")
        self.assertEqual(gameDate, "2018/09/02", msg="Text is worng!")

























