from pywinauto.application import Application
from pywinauto import keyboard
import time
import random

#Connect
app = Application(backend="uia").connect(process=1460)
app = app.window(title_re=".*Error Correction Station - .*", )
time.sleep(2)
if app.window(title="Can't Save document with errors").exists():
    app.OK.draw_outline()
else:
    app.Save.draw_outline()



# child_window(title="Can't Save document until all errors are fixed.\r\n"
#                    "Please click OK button if you completed Keying and want to switch to Errors mode.", auto_id="65535", control_type="Text")






# app.UserLoginfailed.print_control_identifiers()
# print(wnd_name.GetProperties())
# .draw_outline()