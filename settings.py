# global variables for the project
import time
import json

def get_config(l_variable_name):
    l_variable_value = []
    s_file_path='ma_config.json'

    time.sleep(0.5)
    try: # load values from configuration file
        with open(s_file_path) as file:
            config = json.load(file)
            for i in l_variable_name: l_variable_value.append(config[i])
        return 1,l_variable_value
    except Exception as e: # use default values
        print(e)
        return 0,e


def set_config(l_variable_name, l_variable_value):
    s_file_path='ma_config.json'

    try:
        with open(s_file_path) as f:
            data = json.load(f)
            for i in list(range(len(l_variable_name))): 
                data[l_variable_name[i]] = data[l_variable_name[i]].replace(data[l_variable_name[i]],l_variable_value[i])

        with open(s_file_path, 'w') as f:
            json.dump(data, f, indent=4)

            return 1,"OK"
    except Exception as e: # use default values
        print(e)
        return 0,e


def init():

    global l_music_list
    l_music_list = []

    global s_current_music
    s_current_music = ""

    global s_next_music
    s_next_music = ""