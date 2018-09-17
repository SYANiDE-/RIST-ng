#!/usr/bin/env python3
import model, processing
import pyforms, pickle
import webbrowser
import pysettings
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlButton
from pyforms.controls import ControlLabel
# from pyforms.controls import ControlWeb
from os import path, makedirs
from time import sleep

NOTES="""\
### Dependencies:
pysettings          (pip)
pyforms             (pip)
python-pyqt5        (pacman)
opencv-python       (pip)
IPy                 (pip)
python-selenium     (pip)
"""

Version="1.0"
Codename="Grumpy"
Persist="RIST-ng_persist"
Persist_settings="RIST-ng.persist_settings"     # functions and Min, Full
Persist_options="RIST-ng.persist_options"       # browser, always_on_top
OBJS = model.methods._return(model.methods)     # tuple;    #static
WORKING_SET = []                                # list;     #volatile
OPTS = {'browser':1, 'selenium':0, 'always_on_top':0}         # dict;     #static
WORKING_OPT = {}                                # dict;     #volatile
SELENIUMS = { 
    0:'Chrome', 1:'Edge', 2:'Firefox', 3:'Ie', 4:'Opera', 5:'Safari' 
}
BROWSERS = {
    0:'mozilla', 1:'firefox', 2:'netscape', 3:'galeon', 4:'epiphany', 
    5:'skipstone', 6:'kfmclient', 7:'konqueror', 8:'kfm', 9:'mosaic',
    10:'opera', 11:'grail', 12:'links', 13:'elinks', 14:'lynx', 
    15:'w3m', 16:'windows-default', 17:'macosx', 18:'safari', 19:'google-chrome',
    20:'chrome', 21:'chromium', 22:'chromium-browser'
}


class mainWindow(BaseWidget):
    ## Main GUI window
    def __init__(self):
        BaseWidget.__init__(self,"RIST-ng v%s \"%s\"" % (Version, Codename))
        self._show_project()
        self.formset = [('_IoC', '_min', '_full', '_settings'), ' ']
        self._IoC = ControlText("IoC: ")
        self._min, self._min.value = ControlButton("Min"), self._minACTION
        self._full, self._full.value = ControlButton("Full"), self._fullACTION
        self._settings, self._settings.value = ControlButton("Settings"), self._settingsACTION

    def _minACTION(self):
        global WORKING_SET
        global WORKING_OPT
        IoC = (self._IoC.value).replace(" ", "")
        self._IoC.value = ""
        work = processing.worker(IoC, WORKING_SET, WORKING_OPT, 1)
        
    def _fullACTION(self):
        global WORKING_SET
        global WORKING_OPT
        self.settings_window = settingsWindow()
        self.settings_window.parent = self
        self.settings_window.__refresh__()
        IoC = (self._IoC.value).replace(" ", "")
        self._IoC.value = ""
        work = processing.worker(IoC, WORKING_SET, WORKING_OPT, 2)

    def _settingsACTION(self):
        # pyforms.start_app(settingsWindow, geometry=(800,600, 800,600))
        self.settings_window = settingsWindow()
        self.settings_window.parent = self
        self.settings_window.show()

    def _show_project(self):
        global BROWSERS
        global WORKING_OPT
        # self.project_window = projectWindow(BROWSERS, WORKING_OPT)
        # self.project_window.parent = self
        # self.project_window.show()
        webbrowser.open("https://github.com/SYANiDE-/RIST-ng")



class settingsWindow(BaseWidget):
    def __init__(self):
        global OBJS
        global WORKING_SET
        global WORKING_OPT
        BaseWidget.__init__(self,"Settings")
        self.formset = [('_user_settings'),('_user_options',),('_help','_save'),' ']
        self._user_settings = ControlTextArea("")     # reputation source functions and Min,Full settings 
        self._user_options = ControlTextArea("")     # options
        # self._browser_help = ControlTextArea("",readonly=True, autoscroll=False)
        self._help, self._help.value = ControlButton("Help"), self._helpACTION
        self._save, self._save.value = ControlButton("Save"), self._saveACTION
        for name, setting in OBJS:
            self._user_settings.__add__("%s:%s" % (name, setting))
        for name, setting in OPTS.items():
            self._user_options.__add__("%s:%s" % (name, setting))
        self.__config__()

    def __config__(self):
        if not path.exists(Persist):
            makedirs(Persist)
        if not path.exists(Persist+path.sep+Persist_settings):
            self.__save__()
        if not path.exists(Persist+path.sep+Persist_options):
            self.__save__()
        else:
            self.__load__()

    def _helpACTION(self): 
        self.help_window = helpWindow()
        self.help_window.parent = self
        self.help_window.show()

    def _saveACTION(self): 
        self.__save__()

    def __save__(self):
        pickle.dump(self._user_settings.value,  open(Persist+path.sep+Persist_settings, "wb"))
        pickle.dump(self._user_options.value,  open(Persist+path.sep+Persist_options, "wb"))
        self.__refresh__()

    def __load__(self):
        self._user_settings.value = pickle.load(open(Persist+path.sep+Persist_settings, 'rb'))
        self._user_options.value = pickle.load(open(Persist+path.sep+Persist_options, 'rb'))
        self.__refresh__()
                    
    def __refresh__(self):
        global OBJS
        global WORKING_SET
        global WORKING_OPT
        WORKING_SET = []
        WORKING_OPT = {}
        for item in self._user_settings.value.split("\n"):
            name, setting = item.split(":")
            for lineitem in OBJS:
                if lineitem[0] == name:
                    WORKING_SET.append([name, setting])
        for item in self._user_options.value.split("\n"):
            name, setting = item.split(":")
            WORKING_OPT[name]=setting

class helpWindow(BaseWidget):
    def __init__(self):
        BaseWidget.__init__(self,"Help - RIST-ng")
        self.Github = ControlTextArea("")
        self.Github.value = """
URL target methods are prefixed with 'u_'
Domain target methods are prefixed with 'd_'
IP target methods are prefixed with 'i_'


The number on the end after the semicolon (:) defines button behavior
in relation to the target method:
    0 None
    1 Min will trigger
    2 Full will trigger
    3 Both will trigger


RIST-ng Options:
    browser - browser to use in simple cases (typically when GET request)
            - Opens in new TAB
    selenium - browser to use for visit automation (typically when POST request)
            - Opens in new WINDOW
    always_on_top - (currently unimplimented) - RIST-ng window stays on top:  0=off, 1=on


Options for "browser":
%s


Options for "selenium" automated queries:
%s
""" % ( 
        ''.join(["%s=%s\n" % (x, y) for x, y in BROWSERS.items()]),
        ''.join(["%s=%s\n" % (x, y) for x, y in SELENIUMS.items()])    )

# class projectWindow(BaseWidget):
#     def __init__(self, BROWSERS, WORKING_OPT):
#         BaseWidget.__init__(self,"RIST-ng.py Github home")
#         # self.Github, self.Github.value = ControlWeb(""), "https://github.com/SYANiDE-/RIST-ng"    
#         # BR = webbrowser.get(BROWSERS[int(WORKING_OPT['browser'])])



if __name__=="__main__":  
    pyforms.start_app(mainWindow, geometry=(500,20, 500,20))

