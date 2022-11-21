# D:/Patrik/Musics
#import tkinter as tk
import os
import sys
import pygame
import time
import pathlib
import json 
import random
import keyboard


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
        self._n_length = round(pygame.mixer.Sound(_path).get_length())
        print(self._n_length)




if __name__ == '__main__':
    # test the functions

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
    
    
    for path in music._l_music_order:

        # lenght, name of music
        print(f"Lenght of music = {music._n_length}")
        print(f"Name of music : {music._l_music_path[path].name}")

        # load & play music
        pygame.mixer.music.load(music._l_music_path[path])
        pygame.mixer.music.play()


        #b_end_event = False
        b_music_stopped = False
        b_running = True
        while b_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    b_running = False

                if event.type == n_song_end:
                    print('music end event')
                    b_running = False
            
            if keyboard.is_pressed('p'):
                print("music paused")
                pygame.mixer.music.pause()
                continue
            if keyboard.is_pressed('u'):
                print("music unpause")
                pygame.mixer.music.unpause()
                continue
            if keyboard.is_pressed('n'):
                print("next song...")
                break
            if keyboard.is_pressed('s'):
                b_music_stopped = True
                pygame.mixer.music.stop()
                break
        
        if b_music_stopped:
            break
            

    pygame.quit()
    print("End of program")