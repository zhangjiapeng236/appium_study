#-*- encoding = utf-8 -*-
import unittest
from initDevice import *
from ParametrizedCase import *
from threading import Lock
from myFindElement import *
from ddt import ddt,data,unpack
lock = Lock()


@ddt
class testCase1(ParametrizedTestCase):

    def setUp(self):
        lock.acquire()
        self.device = initDevice('projectDeviceConfig\\feitvConfig.yaml',self.param)
        self.driver = self.device.getDeriver()
        lock.release()
        self.myDriver = MyFindElement(self.driver, "elementsConfig\\feitv.yaml")
        self.myDriver.findElement("xpath", "allow").click()

    def tearDown(self):
        print(self.myDriver.creathtml())
        # self.driver.close_app()
        # self.driver.quit()
        # print('pass')

    @data(["appletest23@neuqa.com","111111"])
    @unpack
    def test_search(self, user, psw):
        self.myDriver.findElement("className", "enterMenu").click()
        self.myDriver.findElement("id", "enterSigin").click()
        self.myDriver.findElement("id", "username").send_keys(user)
        self.myDriver.findElement("id", "password").send_keys(psw)
        self.myDriver.findElement("id", "siginButton").click()
        self.myDriver.is_toast_exist("loginSuccess")









