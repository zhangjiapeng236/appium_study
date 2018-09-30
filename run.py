import re

from myThread import *
from testCase.NBA.NBA_accountCase import testSuit_Account_login as case1
from testCase.NBA.NBA_onboardingCase import testSuit_onboarding_UI as case2
from testCase.NBA.NBA_myAccountPageCase import testSuit_MyAccount_teamsTap as case3
from testCase.NBA.NBA_myAccountPageCase import testSuit_MyAccount_videosTap as case4
from testCase.NBA.NBA_myAccountPageCase import testSuit_MyAccount_playersTap as case5
from testCase.NBA.NBA_accountCase import testSuit_Account_subscription as case6
from testCase.NBA.NBA_accountCase import testSuit_Account_regist as case7

if __name__ == '__main__':
    reportOutput = True
    out = os.popen('adb devices')
    serials = []
    runCase = [case1,case2,case4,case5,case6,case7]

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




