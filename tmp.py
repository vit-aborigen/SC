from pywinauto.application import Application
import subprocess
import time
import random

path = "E:\\SC\\EcsWithDelays\\Error Correction.exe"
name = "Error Correction Station"
process = subprocess.Popen(path)

#Connect
app = Application(backend="uia").connect(process=process.pid)
time.sleep(2)

if app.Dialog.window(title_re=".*Another instance of.*", auto_id="65535", control_type="Text").exists():
    app.Dialog.No.click()

app[name].File.select()
app[name].Connect.select()

#Login
app = app['Error Correction StationDialog']
app.Connect.click()


app.Edit.set_edit_text('1')
app.ComboBox.Edit.set_text('1')
app.OK.click()

app.KeyEntryButton.click()

list_box = app.KeyEntryprojectDialog.ListBox
projects_list = list_box.texts()
# Todo: Improvement: choose project randomly
# app.KeyEntryprojectDialog.ListBox[projects_list[0]].invoke()
list_box.ListItem0.select()
app.KeyEntryprojectDialog.OkButton.click()



# app.UserLoginfailed.print_control_identifiers()
# print(wnd_name.GetProperties())
# .draw_outline()