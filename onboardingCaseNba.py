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
        # self.driver.close_app()
        # self.driver.quit()
        port = self.device.getPort()
        killport(port)
        time.sleep(3)

    @unittest.skip("not need")
    def test_onboarding_DL(self):
        for i in range(3):
            for i in range(2):
                location = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/image_view").location
                size = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/image_view").size
                x = location['x']
                y = location['y']
                width = size['width']
                height = size['height']
                self.driver.swipe(x + width * 0.8, y, x, y, 500 )
                time.sleep(2)
            for i in range(2):
                location = self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/image_view").location
                size = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/image_view").size
                x = location['x']
                y = location['y']
                width = size['width']
                height = size['height']
                self.driver.swipe(x, y, x + width * 0.8, y, 500)
                time.sleep(2)

    def test_myFavoriteTeam(self):
        #login an account
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/sign").click()
        try:
            self.myDriver.findElement("xpath", "//*[@text='NONE OF THE ABOVE']").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/register_useremailaddress").send_keys(
            "eloy0831@qq.com")
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/login_password").send_keys("111111")
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/sign_in_button").click()
        #Enter to my favorite team page, remove my fav team
        try:
            while True:
                self.myDriver.findElement("xpath","(//android.support.v7.widget.RecyclerView[@resource-id=\
                'com.nbaimd.gametime.nba2011:id/my_fav_team_list']/android.widget.FrameLayout)[1]").click()
                print("Remove a team successfully!")
        except Exception:
            errorMsg = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/favorite_player_error_msg").text
            print(errorMsg)

        #add my fav team
        for i in range(6):
            self.myDriver.findElement("xpath", "(//android.support.v7.widget.RecyclerView[@resource-id=\
            'com.nbaimd.gametime.nba2011:id/fav_team_list']/android.widget.FrameLayout)[1]").click()
            print("Add a team successfully!")
        toast_loc = ("xpath", ".//*[contains(@text,'The number of your favorites has reached the maximum.')]")
        element = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        print(element.text)
        self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/onboarding_skip").click()

    def test_notifications(self):
        # login an account
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/sign").click()
        try:
            self.myDriver.findElement("xpath", "//*[@text='NONE OF THE ABOVE']").click()
        except Exception:
            print("APP not show smart lock")
            pass
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/register_useremailaddress").send_keys(
            "eloy0831@qq.com")
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/login_password").send_keys("111111")
        self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/sign_in_button").click()


