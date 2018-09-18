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
        self.myDriver = MyFindElement(self.driver)
        try:
            self.myDriver.findElement("xpath","//*[@text='OK']").click()
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
            self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/sign").click()
            try:
                self.myDriver.findElement("xpath", "//*[@text='NONE OF THE ABOVE']").click()
            except Exception:
                print("APP not show smart lock")
                pass

            self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/register_useremailaddress").send_keys(
                "eloy@0831@qq.com")
            self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/login_password").send_keys("111111")
            self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/sign_in_button").click()

            toast_loc = ("xpath", ".//*[contains(@text,'Login successful!')]")
            element = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            print(element.text)









