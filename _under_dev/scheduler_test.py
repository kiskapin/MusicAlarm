import schedule
import time

def test():
    print("This is the job")

if __name__ == '__main__':
    while True:
        
        schedule.every().monday.at("10:01").do(test)
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        print(schedule.get_jobs())
        time.sleep(5)