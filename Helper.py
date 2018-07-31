import datetime
now = datetime.datetime.now()
def current_time():
    return '[{:02}:{:02}:{:02}]'.format(now.hour, now.minute, now.second)

def batch_date():
    return '{:02}{:02}{:04}'.format(now.month, now.day, now.year)