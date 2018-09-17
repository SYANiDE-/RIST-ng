#!/usr/bin/env python3
import model
import threading
from IPy import IP
import webbrowser as WB
from selenium import webdriver


class sanity():
    def __init__(self, IoC):
        self.types = ["d_", "u_", "i_"]
        self.IoC = IoC

    def check(self):
        if self.__isIP__():
            return self.types[2] # i_*
        elif self.__isURL__():
            return self.types[1] # u_*
        else:
            return self.types[0] # d_*
        
    def __isIP__(self):
        try:
            IP(self.IoC)
        except ValueError:
            return False
        return True

    def __isURL__(self):
        URL = ["%", "?", "=", "/", ":"]
        for item in URL:
            if item in self.IoC:
                return True
        return False


class worker():
    def __init__(self, IoC, WORKING_SET, WORKING_OPT, user_choice):
        self.BrowserDict = {
            0:'mozilla', 1:'firefox', 2:'netscape', 3:'galeon', 4:'epiphany',
            5:'skipstone', 6:'kfmclient', 7:'konqueror', 8:'kfm', 9:'mosaic',
            10:'opera', 11:'grail', 12:'links', 13:'elinks', 14:'lynx',
            15:'w3m', 16:'windows-default', 17:'macosx', 18:'safari', 19:'google-chrome',
            20:'chrome', 21:'chromium', 22:'chromium-browser'
        }
        self.SeleniumDict = {
            0:'Chrome', 1:'Edge', 2:'Firefox', 3:'Ie', 4:'Opera', 5:'Safari'
        }
        self.IoC = IoC
        self.IoC_type = sanity(self.IoC).check()
        self.WORKING_SET = []
        self.WORKING_OPT = {}
        self.user_choice = user_choice
        for item in WORKING_SET:
            self.WORKING_SET.append(item)
        for key, val in WORKING_OPT.items():
            self.WORKING_OPT[key] = val
        self.scope()

    def scope(self):
        jobs_list = []
        BR = WB.get(self.BrowserDict[int(self.WORKING_OPT['browser'])])
        SE = getattr(webdriver, self.SeleniumDict[int(self.WORKING_OPT['selenium'])])
        for WS in self.WORKING_SET:
            if WS[0].startswith(self.IoC_type):
                if int(WS[1]) == int(3) or int(WS[1]) == int(self.user_choice):
                    thread = threading.Thread(target=self.worker, args=(WS[0], BR, SE))
                    thread.setDaemon(True)
                    jobs_list.append(thread)
        for j in jobs_list:
            j.start()

    def worker(self, name, BR, SE):
        Methods = model.methods(self.WORKING_SET, self.WORKING_OPT, BR, SE)
        trigger = getattr(Methods, name)
        trigger(IoC=self.IoC)  # this is the call





