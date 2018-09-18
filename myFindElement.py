from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class MyFindElement():
    def __init__(self,driver):
        self.driver = driver


    def findElement(self,By,element):
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


    def findElements(self, By, element):
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

