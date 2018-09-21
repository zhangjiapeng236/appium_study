import re
import os
from myThread import *
from testCase.NBA_onboardingCase import testCase as case2
from testCase.NBA_accountCase import testCase1 as case1


if __name__ == '__main__':
    out = os.popen('adb devices')
    serials = []
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
            device = myThread(serial, case2)
            device.start()
            print("start! {}".format(serial))


