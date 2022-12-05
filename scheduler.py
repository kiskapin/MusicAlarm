# Schedule Library imported
import schedule
import time
import json
import settings

# Functions setup
def work():
	print("Study and work hard")

def set_alarm_time():

    l_wd_time = settings.get_config(['wd_hour','wd_minute'])[1]
    l_we_time = settings.get_config(['we_hour','we_minute'])[1]
    
    # Task scheduling
    # Every weekday at 
    schedule.every().day.at("00:00").do(bedtime)


# Loop so that the scheduling task
# keeps on running all time.

if __name__ == '__main__':

    while True:

        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
