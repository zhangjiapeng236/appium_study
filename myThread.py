#-*- utf-8 -*-
import threading
from loginCaseFeitv import *



class myThread(threading.Thread):
    Cases = []
    def __init__(self, serial, *testCase):
        super(myThread, self).__init__()
        self.serial = serial
        for i in testCase:
            self.Cases.append(i)



    def run(self):
        suite = unittest.TestSuite()
        for i in self.Cases:
            suite.addTest(ParametrizedTestCase.parametrize(i, param=self.serial))
        unittest.TextTestRunner(verbosity=2).run(suite)





