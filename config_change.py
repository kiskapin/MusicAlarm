import json 
import time

def read_status(s_file_path='ma_config.json'):
    try: # load values from configuration file
        with open(s_file_path) as file:
            config = json.load(file)
            s_status = config['music_status']
        return 1,s_status
    except Exception as e: # use default values
        print(e)
        return 0,e

def set_def_status(s_file_path='ma_config.json'):
    try:
        with open(s_file_path) as f:
            data = json.load(f)
            data['music_status'] = data['music_status'].replace(data['music_status'],'szuper')
            print("eddig ok")

        with open(s_file_path, 'w') as f:
            json.dump(data, f)

            return 1,"OK"
    except Exception as e: # use default values
        print(e)
        return 0,e

if __name__ == "__main__":

    global_status = "Play"
    print(global_status)
    while global_status == "Play":
        global_status = read_status()[1]
        time.sleep(0.5)

    print(global_status)
    set_def_status()
    print("status changed")
    global_status = read_status()[1]
    print(global_status)