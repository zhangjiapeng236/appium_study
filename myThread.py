#-*- utf-8 -*-

import HTMLTestRunner
import threading
from threading import Lock
from testCase.Feitv.Feitv_loginCase import *
lock = Lock()


class myThread(threading.Thread):
    Cases = []
    def __init__(self, serial, case = [], report = False):
        super(myThread, self).__init__()
        self.report = report
        self.Cases = case
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
        if self.report == 1:
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
            lock.acquire()
            with open(report_path, 'wb') as report:
                runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title, description=desc)
                runner.run(suite)
            report.close()
            killport(self.port)
            lock.release()
        else:
            unittest.TextTestRunner(verbosity=2).run(suite)
