import re
from myThread import *
from loginCaseNba import testCase1 as case1
from onboardingCaseNba import testCase1 as case2




if __name__ == '__main__':
    out = os.popen('adb devices')
    serials = []
    for i in out.readlines():
        if 'List of devices' in i or 'deamon' in i or 'offline' \
                in i or 'unauthorized' in i or len(i) < 5:
            pass
        else:
            serials = serials + re.findall('(.*)\tdevice', i)
    for serial in serials:
        device = myThread(serial,case2)
        device.start()
        print("start! {}".format(serial))


