# D:/Patrik/Musics
#import tkinter as tk
#import os
import settings
import sys
import pygame
import time
import pathlib
import json 
import random


def get_sys():
    sys_name = ''
    status = 1
    if sys.platform == "linux" or sys.platform == "linux2":
        sys_name = 'linux'
    elif sys.platform == "darwin":
        sys_name = 'OS X'
    elif sys.platform == "win32":
        sys_name = 'Windows'
    else:
        sys_name = 'No system recognised, exiting...'
        status = 0
    
    return status,sys_name

class Music():

    def __init__(self):
        self._s_music_folder = '.\Musics'
        self._l_music_order = list(range(1))
        self._n_length = 20

    def list(self, s_file_path='ma_config.json'):
        try: # load values from configuration file
            with open(s_file_path) as file:
                config = json.load(file)
                if config['music_folder'] != "":
                    self._s_music_folder = config['music_folder']
                else:
                    self._s_music_folder = ".\Musics"
                self._l_music_path = list(pathlib.Path(self._s_music_folder).glob('*.mp3'))
                self._l_music_order = list(range(len(self._l_music_path)))
        except Exception as e: # use default values
            print(e)
            print('No music folder has been defined')
            print('\tHint: Set music_folder in ma_config.json file')
            

    def length(self,_path):
        print(_path)
        self._n_length = round(pygame.mixer.Sound(_path).get_length())


def set_status(_s_status_in='play'):
    s_file_path='ma_config.json'
    try:
        with open(s_file_path) as f:
            data = json.load(f)
            data['music_status'] = data['music_status'].replace(data['music_status'],_s_status_in)

        with open(s_file_path, 'w') as f:
            json.dump(data, f, indent=4)

            return 1,"OK"
    except Exception as e: # use default values
        print(e)
        return 0,e




#if __name__ == '__main__':
def main():
    # test the functions
    settings.set_config(['music_status'],['play'])

    if get_sys()[0] == 1:
        print(get_sys()[1])
    else:
        print('ERROR')
        print(get_sys()[1]) 

    
    # set basic variables
    music = Music()
    pygame.init()

    # List the path from the config file / default musics
    music.list()
    
    n_song_end = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(n_song_end)

    random.shuffle(music._l_music_order)


    # test only one song
    #pygame.mixer.music.load(music._l_music_path[1])
    
    # get the limit of the music number
    i_music_limit = int(settings.get_config(['music_limit'])[1][0])
    for i in music._l_music_order[:i_music_limit]:
        # lenght, name of music
        music.length(music._l_music_path[i])
        print(f"Lenght of music = {music._n_length} sec")
        print(f"Name of music : {music._l_music_path[i].name}")
        settings.set_config(['current_music'],[music._l_music_path[i].name])

        # set volume + load & play music
        _n_volume = float(settings.get_config(['volume'])[1][0]/100)
        pygame.mixer.music.load(f"{music._l_music_path[i]}")
        print(f"def volume: {pygame.mixer.music.get_volume()}")
        pygame.mixer.music.set_volume(_n_volume)
        print(f"new volume: {pygame.mixer.music.get_volume()}")
        pygame.mixer.music.play()
        print(f"after music starts volume: {pygame.mixer.music.get_volume()}")


        #b_end_event = False
        b_music_stopped = False
        b_running = True
        _s_prev_status = settings.get_config(['music_status'])[1][0].lower()

        while b_running:
            i_counter = 0

            _s_status = settings.get_config(['music_status'])[1][0].lower()
            _n_volume = float(settings.get_config(['volume'])[1][0]/100)
            pygame.mixer.music.set_volume(_n_volume)
            #print(f"new volume - while loop: {pygame.mixer.music.get_volume()}")

            if _s_prev_status == _s_status:
                i_counter = 1
            else:
                _s_prev_status = _s_status

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    b_running = False

                if event.type == n_song_end:
                    print('music end event')
                    b_running = False

            if _s_status == "pause" and i_counter == 0:
                print("music paused")
                pygame.mixer.music.pause()
                continue
            if _s_status == "unpause" and i_counter == 0:
                print("music unpause")
                pygame.mixer.music.unpause()
                continue
            if _s_status == "next" and i_counter == 0:
                print("next song...")
                settings.set_config(['music_status'],['play'])
                break
            if _s_status == "stop" and i_counter == 0:
                b_music_stopped = True
                pygame.mixer.music.stop()
                break
        
        if b_music_stopped:
            break
            
    
    settings.set_config(['current_music'],['-'])
    settings.set_config(['music_status'],['play'])
    pygame.quit()
    print("End of program")

if __name__ == '__main__':
    print("Executed as main script")
    main()