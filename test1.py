#coding:utf-8
import time
import os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import yaml
import threading
from appiumServer import AppiumServer
#PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
from initDevice import *
from myFindElement import *






def testcase(serial,port):
    desired_caps = {}
    file = open('projectDeviceConfig\\nbaConfig.yaml', 'r')
    data = yaml.load(file)
    desired = data.get(serial)
    desired_caps['platformName'] = desired['platformName']
    desired_caps['platformVersion'] = desired['platformVersion']
    desired_caps['deviceName'] = desired['deviceName']
    desired_caps['app'] = desired['app']
    desired_caps['appActivity'] = desired['appActivity']
    desired_caps['appPackage'] = desired['appPackage']
    desired_caps['udid'] = desired['udid']
    port = desired['port']
    desired_caps['automationName'] = 'Uiautomator2'  # for get toast info
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True
    s = AppiumServer()
    s.start_appium('127.0.0.1',port)
    time.sleep(3)

    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), desired_caps)
    mydriver = MyFindElement(driver)



    mydriver.findElement("xpath","//*[@text='OK']").click()
    #element.click()
            # WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath(
            # "//*[@text='OK']").is_displayed())
            # driver.find_element_by_xpath("//*[@text='OK']").click()

    WebDriverWait(driver,10).until(lambda the_driver: the_driver.find_element_by_id("com.nbaimd.gametime.nba2011:id/sign").is_displayed())
    driver.find_element_by_id("com.nbaimd.gametime.nba2011:id/sign").click()
    try:
        WebDriverWait(driver, 5).until(lambda the_driver: the_driver.find_element_by_xpath(
        "//*[@text='以上都不是']").is_displayed())
        driver.find_element_by_xpath("//*[@text='以上都不是']").click()
    except Exception:
        print("APP not show smart lock")
        pass
    WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id("com.nbaimd.gametime.nba2011:id/register_useremailaddress").is_displayed())
    driver.find_element_by_id("com.nbaimd.gametime.nba2011:id/register_useremailaddress").send_keys("eloy0831@qq.com")
    WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id(
        "com.nbaimd.gametime.nba2011:id/login_password").is_displayed())
    driver.find_element_by_id("com.nbaimd.gametime.nba2011:id/login_password").send_keys("111111")
    WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_id(
            "com.nbaimd.gametime.nba2011:id/sign_in_button").is_displayed())
    driver.find_element_by_id("com.nbaimd.gametime.nba2011:id/sign_in_button").click()


    print(u"登录成功")
    time.sleep(5)
    driver.quit()
    #killport(port)




if __name__=="__main__":
    s=AppiumServer()
    s.start_appium('127.0.0.1',4726)


    # s.start_appium('127.0.0.1',4725)
    #
    # #t1= threading.Thread(target=testcase,args=('SumsungS7',4725))
    t2= threading.Thread(target=testcase,args=('FA68Z0304192',4726))
    # #t1.start()
    t2.start()
    # driver1 = initDevice('QA-055',4726)
    # #driver1 = devices1.initDevice(4726)
    # driver1.findElemntBy('id')




