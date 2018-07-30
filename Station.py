from pywinauto.application import Application
import sys, os

class SCApplication(object):
    isOpen = False
    isConnected = False #flag will be set by checking Main menu LogIn button (enabled == False, disabled == True)

    def __init__(self):
        print("path")

    def isOpen(self):
        pass

    def isConnected(self):
        pass

    def start(self, isRestart = False):
        pass

    def connect(self, server_name, user, password, isReconnect = False):
        pass

    def close(self):
        pass

test = SCApplication()

# #first_run
# app =
# main_window = app[u'Error Correction Station']
# main_window.wait('ready')
# connected = False # is application connected
#
# menu_item_connect = main_window.menu_item(u'&File->Connect')
# menu_item_disconnect = main_window.menu_item('&File->Disconnect')
# print(menu_item_connect.is_enabled(), menu_item_disconnect.is_enabled())