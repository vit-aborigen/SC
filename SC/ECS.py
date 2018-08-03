from SC import Station
from pywinauto import keyboard
import testpath
import sys

class ErrorCorrectionStation(Station.SCApplication):
    station_name = u"Error Correction Station"
    servers_list = {}

    def __init__(self, ECS_path):
        path = sys.argv[1] if len(sys.argv) > 1 else ECS_path
        testpath.assert_isfile(path, True, 'Incorrect path to ECS executable')
        super().__init__(path)

    def fix_errors(self, mode):
        self.app.window(title_re=".*Error Correction Station - .*", ).wait('visible')
        app = self.app.window(title_re=".*Error Correction Station - .*", )
        if not app.Pane22.OnlyErrorFields.get_toggle_state():
            app.Pane22.OnlyErrorFields.click()

        error_list = app.Pane22.child_window(auto_id="_lvRuleErrors", control_type="List").texts()
        if mode == 'KeyEntry':
            for _field, _error in error_list[1:]:
                # ToDO document errors stored here. some logic would be nice (etc Date, TFN, ABN format)
                # Do some checks
                if _error == 'Invalid date!':
                    keyboard.SendKeys('{ENTER 2}')
                keyboard.SendKeys('{ENTER}')
                app.Dialog.ContinueAnyway.click()
            app.Dialog.Save.click()

