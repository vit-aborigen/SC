from pywinauto.application import Application
import subprocess
import time

path = "C:\\Test\\EcsWithDelays\\Error Correction.exe"
name = "Error Correction Station"
process = subprocess.Popen(path)

#Connect
app = Application(backend="uia").connect(process=process.pid)
app[name].File.select()
app[name].Connect.select()

#Login
app = app['Error Correction StationDialog']
app.Connect.click()


app.Edit.set_edit_text('test')
app.ComboBox.Edit.set_text('test')
app.OK.click()

# if app['User Login Failed'].exists():
#     app.Dialog.OK.click()

print(app['User Login Failed'].exists())
