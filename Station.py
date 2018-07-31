from pywinauto.application import Application
import subprocess
import time
import Helper


class SCApplication(object):
    isOpen = False
    isConnected = False
    path = None
    process = None
    app = None

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

    def connect(self, station_name, server_name, isReconnect = False):
        try:
            self.app = Application(backend="uia").connect(process=self.process.pid)
        except:
            print('Cannot find {} instance'.format(station_name))
            return None

        app = self.app
        time.sleep(3)
        while not app.windows():
            time.sleep(1)

        # Checking whether another instances exist. More than one instance is allowed atm.
        if app.Dialog.window(title_re=".*Another instance of.*", auto_id="65535", control_type="Text").exists():
            app.Dialog.No.click()

        app[station_name].File.select()
        app[station_name].Connect.select()

        #Login
        app = app[station_name + 'Dialog']
        app.ComboBox.Edit.set_text(server_name)
        app.Connect.click()
        print('{} Station connected to server {}'.format(Helper.current_time(), server_name))

    def login(self, station_name, user, password):
        app = self.app[station_name + 'Dialog']
        app.Edit.set_edit_text(user)
        app.ComboBox.Edit.set_text(password)
        app.OK.click()

        # is_credentials_correct = False
        # app = self.app[station_name + 'Dialog']
        # while not is_credentials_correct:
        #     app.Edit.set_edit_text(user)
        #     app.ComboBox.Edit.set_text(password)
        #     app.OK.click()
        #
        #     if app.Dialog.exists():
        #         app.Dialog.OK.click()
        #         raise NotImplemented("Wrong password")
        #         continue
        #     is_credentials_correct = True
        print('{} User {} with password {} has logged in'.format(Helper.current_time(), user, password))
        self.isConnected = True

    def close(self):
        print('{} ECS with PID={} was closed'.format(Helper.current_time(), self.process.pid))
        self.process.terminate()
        self.isConnected = False
        self.isOpen = False