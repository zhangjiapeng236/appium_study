#-*- encoding:utf-8 -*-
import socket
import subprocess
import os
import time
from loginCaseFeitv import *




class AppiumServer():
    # Check port is whether or not used
    def check_port(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            s.shutdown(2)
            print('port %s is uesd !' %port)
            return False
        except:
            print('port %s is available!' %port)
            return True

    #Launch Appium server
    def start_appium(self,host,port):
        errormessage=""
        appium_server_url=""
        bootstrap_port=str(int(port)+10)

        try:
            if self.check_port(host,port):
                cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port)
                print(cmd)
                # launch a process to start appium server
                p = subprocess.Popen(cmd, shell=True, stdout=open('C:/Users/james/Desktop/monkeyrunner/testlog/logs.log','a'), stderr=subprocess.STDOUT)
                p.wait()
                time.sleep(3)

        except Exception as msg:
            errormessage=str(msg)
            print(errormessage)

        return errormessage

#Kill a process by port
def killport(port):
    taskinfo = os.popen('netstat -ano | findstr {}'.format(port))
    line = taskinfo.readline()
    aList = line.split()
    taskinfo.close()
    pid = aList[4]
    os.popen('taskkill /pid %s /f' % pid)
    print("Port:{} has been killed!".format(port))





