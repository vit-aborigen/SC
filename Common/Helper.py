import datetime
datetime.datetime.now()
def current_time():
    return '[{:02}:{:02}:{:02}]'.format(datetime.datetime.now().hour, datetime.datetime.now().minute,
                                        datetime.datetime.now().second)

def batch_date():
    return '{:02}{:02}{:04}'.format(datetime.datetime.now().month, datetime.datetime.now().day,
                                    datetime.datetime.now().year)