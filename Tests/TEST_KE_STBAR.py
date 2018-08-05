# This module is using for testing ECS Key Entry mode
# Test form is Super transfer balance account report
# Automation is created to reproduce filling out 1000 bathes * 10 Forms * 5 fields each

from SC import KE_ECS
from Common import Helper
import random

""" Initial data """
ECS_path = "E:\\SC\\EcsWithDelays\\Error Correction.exe"
sc_servers = {'127.0.0.1':('1', '1')}
server_name = random.choice(list(sc_servers.keys()))
user_name, password = sc_servers[server_name]

""" Data used for KE tests """
test_data = None
memberTFN = random.choice(['{8}{6}{2}{7}{9}{3}{4}{9}{8}', '{1}{2}{3}{4}{5}{6}{7}{8}{9}'])
numberOfFieldsToEdit = 4 # +1 for memberTFN field
moveNFieldDown = '{{DOWN {}}}'.format(random.randint(1, 10))
currentFieldValue = '{R}{a}{n}{d}{o}{m}{SPACE}{v}{a}{l}{u}{e}'
test_data = (memberTFN, numberOfFieldsToEdit, moveNFieldDown, currentFieldValue)

""" Test configuration """
numberOfFormsToProcessPerBatch = 10
numberOfBatchToProcess = 100

""" Test section """
test = KE_ECS.KeyEntry(ECS_path)
test.start(True)
test.connect(test.station_name, server_name)
test.login(test.station_name, user_name, password)
test.load_extension()
for batchNumber in range(numberOfBatchToProcess):
    test.create_batch()
    print('{} --- Batch #{} created'.format(Helper.current_time(), batchNumber + 1))

    for formNumber in range(numberOfFormsToProcessPerBatch):
        test.new_form_barcode()
        isECSRequired = test.process_form(test_data)
        print('{} ------ KE Form #{} saved'.format(Helper.current_time(), formNumber + 1))

        if isECSRequired[1]:
            test.fix_errors("KeyEntry")
            print('{} ------ Form #{} was ECSed'.format(Helper.current_time(), formNumber + 1))
    test.close_batch()
