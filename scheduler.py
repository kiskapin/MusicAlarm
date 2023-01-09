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
    

def set_wd_alarm_time(_l_wd_time):
    # wd = week day
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
    get_alarm_time()
    _l_wd_time_curr = [None]
    _l_we_time_curr = [None]


    # Loop so that the scheduling task keeps on running all time.
    while True:

        # set hours - when the application can sleep
        _n_wd_sleep     = settings.l_wd_time[0]
        _n_we_sleep     = settings.l_we_time[0]

        now = datetime.datetime.now()

        get_alarm_time()
        print(settings.l_wd_time)
        print(settings.l_we_time)
        print(_l_wd_time_curr)
        print(_l_we_time_curr)
        if _l_wd_time_curr != settings.l_wd_time:
            schedule.clear('wd')
            if settings.l_wd_time[0] != "-":
                print("block wd 1")
                set_wd_alarm_time(settings.l_wd_time)
                _l_wd_time_curr = settings.l_wd_time


        if _l_we_time_curr != settings.l_we_time:
            schedule.clear('we')
            if settings.l_we_time[0] != "-":
                print("block we 1")
                set_we_alarm_time(settings.l_we_time)
                _l_we_time_curr = settings.l_we_time
        
        # set hours - when the application can sleep
        if _n_wd_sleep == '-':
            _n_wd_sleep = 0
        if _n_we_sleep == '-':
            _n_we_sleep = 0
        
        print(_n_wd_sleep)
        print(_n_we_sleep)

        print(schedule.get_jobs())
        # Checks whether a scheduled task is pending to run or not
        schedule.run_pending()
        if _n_wd_sleep == 0 and _n_we_sleep == 0 :
            print("WE and WD turned off")
            time.sleep(30*60)
        else:
            if now.hour - 1 == int(_n_wd_sleep) or now.hour == int(_n_wd_sleep) or now.hour+1 == int(_n_wd_sleep) or now.hour - 1 == int(_n_we_sleep) or now.hour == int(_n_we_sleep) or now.hour + 1 == int(_n_we_sleep):
                print(f"TRUE - now.hour= {now.hour}, _l_wd_time_curr= {_l_wd_time_curr}, _l_we_time_curr= {_l_we_time_curr} ")
                time.sleep(60)
            else:
                print(f"FALSE - now.hour= {now.hour}, _l_wd_time_curr= {_l_wd_time_curr}, _l_we_time_curr= {_l_we_time_curr} ")
                time.sleep(10*60)