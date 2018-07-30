import datetime
now = datetime.datetime.now()
def current_time():
    return '[{:02}:{:02}:{:02}]'.format(now.hour, now.minute, now.second)