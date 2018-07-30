from pywinauto.application import Application
from pywinauto import keyboard
import sys, os, subprocess, time, Helper


class SCApplication(object):
    isOpen = False
    isConnected = False
    path = None
    process = None

    def __init__(self, path):
        self.path = path

    def IsOpen(self):
        return self.isOpen

    def IsConnected(self):
        return self.isConnected

    def start(self, isRestart = False):
        if isRestart and self.IsOpen():
            print('{} Restarting ECS with PID={}'.format(Helper.current_time(), self.process.pid))
            self.process.terminate()
            self.process = None
            self.isOpen = False
            self.isConnected = False
        self.process = subprocess.Popen(self.path)
        print('{} ECS with PID={} started'.format(Helper.current_time(), self.process.pid))
        self.isOpen = True

    def connect(self, station_name, server_name, user, password, isReconnect = False):
        # print(wnd_name.GetProperties())
        app = Application().connect(process=self.process.pid)
        while not app.windows():
            time.sleep(1)
        if app.Dialog.exists():
            app.Dialog.No.click()

        main_window = app[station_name].wait('ready', 5, 5)
        main_window.menu_item('File->Connect').click()

        connect_window = app['Connect to server'].wait('ready', 5, 5)
        # THIS IS IT!
        # connect_window.draw_outline()
        # But controls are encapsulated way too deep, so emulating <Enter> is only suitable solution (except coords)
        connect_window.set_focus()
        connect_window.type_keys("{ENTER}")
        print('{} Station connected to server {}'.format(Helper.current_time(), server_name))

        is_credentials_correct = False
        while not is_credentials_correct:
            login_window = app['User LogIn'].wait('ready', 5, 5)
            slow_dropbox = app[u'User LogIn'].Edit2.wait('ready', 5, 5)
            slow_dropbox.set_edit_text(user)
            app[u'User LogIn'].Edit.set_edit_text(password)
            app['User Login'].OK.click()

            if app.Dialog.exists():
                app.Dialog.OK.click()
                raise NotImplemented("Wrong password")
                continue
            is_credentials_correct = True
        print('{} User {} with password {} has logged in'.format(Helper.current_time(), user, password))
        self.isConnected = True

    def close(self):
        pass