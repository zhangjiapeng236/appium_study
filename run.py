import re

from myThread import *
from testCase.NBA.NBA_accountCase import testCase1 as case1
from testCase.NBA.NBA_onboardingCase import testCase as case2
from testCase.NBA.NBA_myAccountPageCase import testCase1 as case3

if __name__ == '__main__':
    reportOutput = True
    out = os.popen('adb devices')
    serials = []
    runCase = [case1, case2, case3]

    for i in out.readlines():
        if 'List of devices' in i or 'deamon' in i or 'offline' \
                in i or 'unauthorized' in i or len(i) < 5:
            pass
        else:
            serials = serials + re.findall('(.*)\tdevice', i)

    if len(serials) == 0:
        print("Current can't find any device connected!")
    else:
        for serial in serials:
            device = myThread(serial, case = runCase, report = reportOutput)
            device.start()
            print("start! {}".format(serial))




