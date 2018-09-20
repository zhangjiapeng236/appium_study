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
            pass

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        port = self.device.getPort()
        killport(port)
        time.sleep(3)

    def test_loginSuccess(self):
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
            self.myDriver.is_toast_exist("Login successful!")








