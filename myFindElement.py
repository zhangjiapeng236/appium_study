from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import yaml
from selenium.webdriver.support import expected_conditions as EC

class MyFindElement():
    TimeOut = 10

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
            WebDriverWait(self.driver, self.TimeOut).until( \
                lambda the_driver: the_driver.find_element_by_id(element))
            return self.driver.find_element_by_id(element)

        elif By == 'xpath':
            WebDriverWait(self.driver, self.TimeOut).until( \
                lambda the_driver: the_driver.find_element_by_xpath(element))
            return self.driver.find_element_by_xpath(element)

        elif By == 'class_name':
            WebDriverWait(self.driver, self.TimeOut).until( \
                lambda the_driver: the_driver.find_element_by_class_name(element))
            return self.driver.find_element_by_class_name(element)

        else:
            print('Don\'t find {} function!'.format(By))

    def findElements(self, By, name):
        element = self.trasitionYaml(name)
        if By == 'id':
            WebDriverWait(self.driver, self.TimeOut).until( \
                lambda the_driver: the_driver.find_elements_by_id(element))
            return self.driver.find_elements_by_id(element)

        elif By == 'xpath':
            WebDriverWait(self.driver, self.TimeOut).until( \
                lambda the_driver: the_driver.find_elements_by_xpath(element))
            return self.driver.find_elements_by_xpath(element)

        elif By == 'class_name':
            WebDriverWait(self.driver, self.TimeOut).until( \
                lambda the_driver: the_driver.find_elements_by_class_name(element))
            return self.driver.find_elements_by_class_name(element)

        else:
            print('Don\'t find {} function!'.format(By))

    def is_toast_exist(self, name,poll_frequency=0.5):
        try:
            element = self.trasitionYaml(name)
            toast_loc = ("xpath", element)
            toast = WebDriverWait(self.driver, self.TimeOut, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            print(toast.text)
        except Exception as errorMsg:
            print(errorMsg)

