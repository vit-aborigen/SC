from SC import ECS
from Common import Helper
import time
from pywinauto import keyboard

class KeyEntry(ECS.ErrorCorrectionStation):
    station_name = u"Error Correction Station"
    def __init__(self, path):
        super().__init__(path)

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

    def create_batch(self):
        app = self.app[self.station_name + 'Dialog']
        app.Dialog2.BatchFields.Edit3.set_text(Helper.batch_date())
        app.Dialog2.OK.click()
        print('{} {} batch date was specified'.format(Helper.current_time(), Helper.batch_date(), ))

    def close_batch(self):
        app = self.app[self.station_name + 'Dialog']
        app.NewFormBarcodeDialog.CloseBatch.click()
        print('{} batch was closed'.format(Helper.current_time()))

    def new_form_barcode(self):
        # new form barcode
        app = self.app[self.station_name + 'Dialog']
        list_box = app.NewFormBarcodeDialog.GroupBox2.ListBox1
        barcodes_list = list_box.texts()
        # Todo: Improvement: choose form barcode randomly
        # list_box.ListItem0.select()
        keyboard.SendKeys('{DOWN}')
        app.NewFormBarcodeDialog.AddForm.click()
        print('{} ------ Form barcode {} was specified'.format(Helper.current_time(), barcodes_list[0]))

    def process_form(self, test_data):
        # Form loading time is very dependent on PC performance. Based on tests loading takes from 5 to 30 sec
        formLoaded = False
        numberOfTries = 3
        self.app.window(title_re=".*Error Correction Station - .*", ).wait('visible')
        while not formLoaded and numberOfTries:
            app = self.app.window(title_re=".*Error Correction Station - .*", )
            if app.Keying.wait('visible', timeout=30):
                formLoaded = True
                break
            numberOfTries -= 1
            time.sleep(10)

        # ToDO: Rewrite hardcoded part
        # Another Medved's or Framework bug
        # memberTFN = random.choice(['862793498', '123456789'])
        # app.Keying.Edit2.set_text(memberTFN)

        # Supposing the very first field is 'MemberTFN'
        memberTFN = test_data[0]
        keyboard.SendKeys(memberTFN)

        numberOfFieldsToEdit = test_data[1]
        while numberOfFieldsToEdit:
            moveNFieldDown = test_data[2]
            keyboard.SendKeys(moveNFieldDown)

            # Setting 'Random value' text for any editable field and 'Checked' for checkboxes:
            currentFieldValue = test_data[3]
            if not app.Keying.Edit2.wrapper_object().get_value():
                keyboard.SendKeys(currentFieldValue)
            else:
                keyboard.SendKeys('{SPACE}')
            numberOfFieldsToEdit -= 1

        keyboard.SendKeys('^s')
        if app.window(title="Confirm Saving of keyed document").exists():
            app.OK.click()
            if app.window(title="Can't Save document with errors").exists():
                app.OK.click()
                return (0, 1) # ECS required
            else:
                app.Save.click()
                return (0, 0) # ECS doesn't required