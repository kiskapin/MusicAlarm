# This script checks every 10 minutes the config json file for alarm timing

import schedule
import time
import json
import datetime

# import custom scripts
import settings
import ma_music_player as mmp



def get_alarm_time():

    settings.l_wd_time = settings.get_config(['wd_hour','wd_minute'])[1]
    settings.l_we_time = settings.get_config(['we_hour','we_minute'])[1]
    


def print_job():
    print("Test function")


def set_wd_alarm_time(_l_wd_time):
    # wd = week day
    print((f"WEEKDAY {_l_wd_time[0]}:{_l_wd_time[1]}"))
    schedule.every().monday.at(f"{_l_wd_time[0]}:{_l_wd_time[1]}").do(mmp.main).tag('wd')
    schedule.every().tuesday.at(f"{_l_wd_time[0]}:{_l_wd_time[1]}").do(mmp.main).tag('wd')
    schedule.every().wednesday.at(f"{_l_wd_time[0]}:{_l_wd_time[1]}").do(mmp.main).tag('wd')
    schedule.every().thursday.at(f"{_l_wd_time[0]}:{_l_wd_time[1]}").do(mmp.main).tag('wd')
    schedule.every().friday.at(f"{_l_wd_time[0]}:{_l_wd_time[1]}").do(mmp.main).tag('wd')


def set_we_alarm_time(_l_we_time):
    # we = week end
    schedule.every().saturday.at(f"{_l_we_time[0]}:{_l_we_time[1]}").do(mmp.main).tag('we')
    schedule.every().sunday.at(f"{_l_we_time[0]}:{_l_we_time[1]}").do(mmp.main).tag('we')


if __name__ == '__main__':
    
    settings.init()

    _l_wd_time_curr = settings.l_wd_time
    _l_we_time_curr = settings.l_we_time


    # Loop so that the scheduling task keeps on running all time.
    while True:

        now = datetime.datetime.now()

        get_alarm_time()
        if _l_wd_time_curr != settings.l_wd_time:
            schedule.clear('wd')
            set_wd_alarm_time(settings.l_wd_time)
            _l_wd_time_curr = settings.l_wd_time

        if _l_we_time_curr != settings.l_we_time:
            schedule.clear('we')
            set_we_alarm_time(settings.l_we_time)
            _l_we_time_curr = settings.l_we_time

        print(_l_we_time_curr)
        print(schedule.get_jobs())
        # Checks whether a scheduled task is pending to run or not
        schedule.run_pending()
        if now.hour - 1 == _l_wd_time_curr[0] or now.hour == _l_wd_time_curr[0] or now.hour - 1 == _l_we_time_curr[0] or now.hour == _l_we_time_curr[0]:
            time.sleep(10)
        else:
            time.sleep(30)
        