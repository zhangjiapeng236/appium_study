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
class testCase1(ParametrizedTestCase):

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




    #@unittest.skip("not need")
    @data(["eloy0831@qq.com","111111"],[" eloy0916@qq.com ","111111"])
    @unpack
    def test_loginSuccessful(self, user, psw):
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







    @unittest.skip("not need")
    @data(["eloy0131@qq.com", "111111"],["eloy0116@qq.com", "111111"])
    @unpack
    def test_loginFail(self, user, psw):
        self.myDriver.findElement("id", "enterSigin").click()
        try:
            self.myDriver.findElement("xpath", "smartLock").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "userBox").send_keys(user)
        self.myDriver.findElement("id", "passwordBox").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginFailed")

    @unittest.skip("not need")
    @data(["eloy", "111111"],["eloy0116@qq.com", ""],["","11111"],["#$%^", "23"])
    @unpack
    def test_loginError(self, user, psw):
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

    @unittest.skip("not need")
    @data(["eloy08311@qq.com"],["eloy"],["eloy0831@qq.com"],[""])
    @unpack
    def test_forgotPassword(self, user):
        self.myDriver.findElement("id", "enterSigin").click()
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


















