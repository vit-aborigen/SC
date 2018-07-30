from pywinauto.application import Application
import Station
import testpath
import sys
import time

class ErrorCorrectionStation(Station.SCApplication):
    station_name = u"Error Correction Station"
    servers_list = {}

    def __init__(self):
        path = sys.argv[1] if len(sys.argv) > 1 else "E:\\SC\\EcsWithDelays\\Error Correction.exe"
        testpath.assert_isfile(path, True, 'Incorrect path to ECS executable')
        super().__init__(path)

    #move to Helper and make choice randomly
    def addServer(self, server_name, user, password):
        if server_name not in self.servers_list.keys():
            self.servers_list[server_name] = [(user, password)]
        else:
            self.servers_list[server_name].append((user, password))


test = ErrorCorrectionStation()
test.start(True)
test.connect(test.station_name, '127.0.0.1', '1', '1')