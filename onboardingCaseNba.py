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

    # def test_onboarding_DL(self):
    #     for i in range(3):
    #         for i in range(2):
    #             location = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/image_view").location
    #             size = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/image_view").size
    #             x = location['x']
    #             y = location['y']
    #             width = size['width']
    #             height = size['height']
    #             self.driver.swipe(x + width * 0.8, y, x, y, 500 )
    #             time.sleep(2)
    #         for i in range(2):
    #             location = self.myDriver.findElement("id", "com.nbaimd.gametime.nba2011:id/image_view").location
    #             size = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/image_view").size
    #             x = location['x']
    #             y = location['y']
    #             width = size['width']
    #             height = size['height']
    #             self.driver.swipe(x, y, x + width * 0.8, y, 500)
    #             time.sleep(2)

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
        # Enter to my favorite team page
        try:
            myFavTeam = self.myDriver.findElement("id","com.nbaimd.gametime.nba2011:id/my_fav_team_list").find_elements_by_class_name("android.widget.FrameLayout")
        except Exception:
            myFavTeam = []
        if len(myFavTeam) > 0:
            for i in range(len(myFavTeam)):
                myFavTeam[i].click()
                time.sleep(2)
                print("Remove a tema! {}".format(i))
        else:
            print('Doesn\'t find my favorite team!')
            pass


