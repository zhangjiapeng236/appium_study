from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import yaml
from selenium.webdriver.support import expected_conditions as EC

class MyFindElement():

    def __init__(self,driver,yamlFile):
        self.driver = driver
        file = open(yamlFile, 'r')
        self.data = yaml.load(file)

    def trasitionYaml(self,key):
        element = self.data[key]
        return element

    def findElement(self,By,name):
        element = self.trasitionYaml(name)
        if By == 'id':
            WebDriverWait(self.driver, 20).until( \
                lambda the_driver: the_driver.find_element_by_id(element))
            return self.driver.find_element_by_id(element)

        elif By == 'xpath':
            WebDriverWait(self.driver, 20).until( \
                lambda the_driver: the_driver.find_element_by_xpath(element))
            return self.driver.find_element_by_xpath(element)

        elif By == 'class_name':
            WebDriverWait(self.driver, 20).until( \
                lambda the_driver: the_driver.find_element_by_class_name(element))
            return self.driver.find_element_by_class_name(element)

        else:
            print('Don\'t find {} function!'.format(By))

    def findElements(self, By, name):
        element = self.trasitionYaml(name)
        if By == 'id':
            WebDriverWait(self.driver, 20).until( \
                lambda the_driver: the_driver.find_elements_by_id(element))
            return self.driver.find_elements_by_id(element)

        elif By == 'xpath':
            WebDriverWait(self.driver, 10).until( \
                lambda the_driver: the_driver.find_elements_by_xpath(element))
            return self.driver.find_elements_by_xpath(element)

        elif By == 'class_name':
            WebDriverWait(self.driver, 20).until( \
                lambda the_driver: the_driver.find_elements_by_class_name(element))
            return self.driver.find_elements_by_class_name(element)

        else:
            print('Don\'t find {} function!'.format(By))

    def is_toast_exist(self, text,timeout=30,poll_frequency=0.5):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" %text)
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            print(text)

        except Exception as errorMsg:
            print(errorMsg)

