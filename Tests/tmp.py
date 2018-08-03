from pywinauto.application import Application
from pywinauto import keyboard
import time
import random

#Connect
app = Application(backend="uia").connect(process=17128)
app = app.window(title_re=".*Error Correction Station - .*", )
time.sleep(2)

app.Pane22.OnlyErrorFields.draw_outline()

# document_error_wnd = app.Pane22.child_window(auto_id="792966", control_type="Pane")
# if not document_error_wnd.OnlyErrorFields.get_toggle_state():
#     document_error_wnd.OnlyErrorFields.click()
#
# mode = 'KeyEntry'
# error_list = document_error_wnd.child_window(auto_id="_lvRuleErrors", control_type="List").texts()
# if mode == 'KeyEntry':
#     for error in range(len(error_list) - 1):
#         keyboard.SendKeys('{ENTER}')
#         app.Dialog.ContinueAnyway.click()
#     app.Dialog.Save.click()






# app.UserLoginfailed.print_control_identifiers()
# print(wnd_name.GetProperties())
# .draw_outline()