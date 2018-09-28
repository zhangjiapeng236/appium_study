from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import yaml
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import os
import unittest
PATH = lambda p: os.path.abspath(
os.path.join(os.path.dirname(__file__), p))


class MyFindElement():
    TimeOut = 10
    pics = []
    picpath = []


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
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_element_by_id(element))
                return self.driver.find_element_by_id(element)
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} element!".format(name))
                raise eMsg

        elif By == 'xpath':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_element_by_xpath(element))
                return self.driver.find_element_by_xpath(element)
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} element!".format(name))
                raise eMsg

        elif By == 'className':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_element_by_class_name(element))
                return self.driver.find_element_by_class_name(element)
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} element!".format(name))
                raise eMsg
        else:
            print('Don\'t find {} function!'.format(By))

    def findElements(self, By, name):
        element = self.trasitionYaml(name)
        if By == 'id':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_elements_by_id(element))
                return self.driver.find_elements_by_id(element)
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} elements!".format(name))
                raise eMsg

        elif By == 'xpath':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_elements_by_xpath(element))
                return self.driver.find_elements_by_xpath(element)
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} elements!".format(name))
                raise eMsg

        elif By == 'className':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_elements_by_class_name(element))
                return self.driver.find_elements_by_class_name(element)
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} elements!".format(name))
                raise eMsg
        else:
            print('Don\'t find {} function!'.format(By))

    def findElement_location(self, By, name):
        element = self.trasitionYaml(name)
        if By == 'id':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_element_by_id(element))
                location = self.driver.find_element_by_id(element).location
                size = self.driver.find_element_by_id(element).size
                locations = {**size, **location}
                return locations
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} element!".format(name))
                raise eMsg

        elif By == 'xpath':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_element_by_xpath(element))
                location = self.driver.find_element_by_xpath(element).location
                size = self.driver.find_element_by_xpath(element).size
                locations = {**size, **location}
                return locations
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} element!".format(name))
                raise eMsg

        elif By == 'className':
            try:
                WebDriverWait(self.driver, self.TimeOut).until( \
                    lambda the_driver: the_driver.find_element_by_class_name(element))
                location = self.driver.find_element_by_class_name(element).location
                size = self.driver.find_element_by_class_name(element).size
                locations = {**size, **location}
                return locations
            except Exception as eMsg:
                self.screenshot()
                print("Can't find {} element!".format(name))
                raise eMsg
        else:
            print('Don\'t find {} function!'.format(By))

    def is_toast_exist(self, name,poll_frequency=0.5):
        try:
            element = self.trasitionYaml(name)
            toast_loc = ("xpath", element)
            toast = WebDriverWait(self.driver, self.TimeOut, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            print(toast.text)
        except Exception as eMsg:
            self.screenshot()
            print("Can not find {} toast!".format(name))
            raise eMsg

    def screenshot(self):
        date = time.strftime("%Y%m%d")
        times = time.strftime("%H%M%S")
        dirname = PATH("./ScreenShot/" + date)
        relDirname = "/appium_study/ScreenShot/" + date
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        pic = times + ".png"
        path = dirname + "\\" + pic
        self.driver.get_screenshot_as_file(path)
        relPath = "localhost:63342" + relDirname + "/" + pic
        html = '<br /><a href=' + relPath + ' target="_blank">' + pic + '</a>'
        htmls = 'htmlbegin' + html + 'htmlend'
        print(htmls)












