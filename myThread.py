#-*- utf-8 -*-
import threading
from appiumServer import *
import HtmlTestRunner
import HTMLTestRunner
from testCase.Feitv_loginCase import *
from threading import Lock
lock = Lock()


class myThread(threading.Thread):
    Cases = []
    def __init__(self, serial, *testCase):
        super(myThread, self).__init__()
        self.Cases = testCase
        self.serial = serial
        file = open("projectDeviceConfig\\commonPort.yaml", 'r')
        data = yaml.load(file)
        desired = data.get(self.serial)
        self.port = desired["port"]
        self.deviceName = desired["deviceName"]
        self.s = AppiumServer()
        self.s.start_appium('127.0.0.1', self.port)
        time.sleep(3)




    def run(self):
        suite = unittest.TestSuite()
        for i in self.Cases:
            suite.addTest(ParametrizedTestCase.parametrize(i, param=self.serial))
        date = time.strftime("%Y%m%d")
        times = time.strftime("%H%M%S")
        path = "./report/" + date + "/"
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass
        report_path = path + times + "_{}_report.html".format(self.deviceName)
        report_title = "Test Report"
        desc = "Appium Test Report detail:"

        with open(report_path, 'wb') as report:
            runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title, description=desc)
            runner.run(suite)
        report.close()
        killport(self.port)




   # date = time.strftime("%Y%m%d_{}".format(self.deviceName))
        # runner = HtmlTestRunner.HTMLTestRunner(output=date)
        # runner.run(suite)
        #unittest.TextTestRunner(verbosity=2).run(suite)
