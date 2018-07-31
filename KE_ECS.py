import ECS
import Helper
import time
from pywinauto import keyboard

class KeyEntry(ECS.ErrorCorrectionStation):
    station_name = u"Error Correction Station"
    def __init__(self):
        super().__init__()

    def load_extension(self):
        app = self.app[self.station_name + 'Dialog']

        # Choosing extension
        app.KeyEntryButton.click()

        # Getting available projects list
        list_box = app.KeyEntryprojectDialog.ListBox
        projects_list = list_box.texts()
        # Todo: Improvement: choose project randomly
        #list_box.ListItem0.select()

        keyboard.SendKeys('{UP}')
        app.KeyEntryprojectDialog.OK.click()

        print('{} Key Entry mode loaded, project: {} was chosen'.format(Helper.current_time(), projects_list[0]))

    def fill_batch(self):
        app = self.app[self.station_name + 'Dialog']
        app.Dialog2.BatchFields.Edit3.set_text(Helper.batch_date())
        app.Dialog2.OK.click()

        # new form barcode
        list_box = app.NewFormBarcodeDialog.GroupBox2.ListBox1
        barcodes_list = list_box.texts()
        # Todo: Improvement: choose form barcode randomly
        # list_box.ListItem0.select()
        keyboard.SendKeys('{DOWN}')
        app.NewFormBarcodeDialog.AddForm.click()
        print('{} Batch date {} and Form barcode {} were specified'.
              format(Helper.current_time(), Helper.batch_date(), barcodes_list[0]))

    def process_form(self):
        pass


test = KeyEntry()
test.start(True)
test.connect(test.station_name, '127.0.0.1')
test.login(test.station_name, '1', '1')
test.load_extension()
test.fill_batch()
time.sleep(10)
test.process_form()


#
# while True:
#     test.start(True)
#     test.connect(test.station_name, '127.0.0.1')
#     test.login(test.station_name, '1', '1')
#     test.close()