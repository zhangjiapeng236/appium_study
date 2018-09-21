#-*- encoding = utf-8 -*-
import unittest
from initDevice import *
from ParametrizedCase import *
from appiumServer import *
from threading import Lock
from appium import webdriver
lock = Lock()



class testCase1(ParametrizedTestCase):

    def setUp(self):
        lock.acquire()
        self.device = initDevice('feitvConfig.yaml',self.param)
        self.driver = self.device.getDeriver()
        lock.release()
        WebDriverWait(self.driver, 20).until(\
            lambda  the_driver: the_driver.find_element_by_xpath("//*[@text='ALLOW']"))
        self.driver.find_element_by_xpath("//*[@text='ALLOW']").click()

        WebDriverWait(self.driver, 20).until(
            lambda the_driver: the_driver.find_element_by_id("ptv.fei:id/search_view").is_displayed())
        self.driver.find_element_by_id("ptv.fei:id/search_view").click()
        port = self.device.getPort()
        killport(port)





    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        print('pass')

    def test_login(self):
       pass

        #self.driver.find_element_by_id("com.nbaimd.gametime.nba2011:id/sign").click()





