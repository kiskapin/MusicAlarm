# D:/Patrik/Musics
import os
import sys
from pygame import mixer
# importing time module
import time
import pathlib
import json 
import tkinter as tk
import random




def get_sys():
    _sys_name = ''
    _status = 1
    if sys.platform == "linux" or sys.platform == "linux2":
        _sys_name = 'linux'
    elif sys.platform == "darwin":
        _sys_name = 'OS X'
    elif sys.platform == "win32":
        _sys_name = 'Windows'
    else:
        _sys_name = 'No system recognised, exiting...'
        _status = 0
    
    return _status,_sys_name

class Music():

    def __init__(self):
        self.IsPaused = False
        self._sMusicFolder = '.\Musics'
        self._lMusicOrder = list(range(1))
        self._length = 20

    def toggleMusic(self):
        if self.IsPaused:
            print("Unpause Music")
            mixer.music.unpause()
            self.IsPaused = False
        else:
            print("Pause Music")
            mixer.music.pause()
            self.IsPaused = True
    def stop(self):
        print("Stop Music")
        mixer.music.stop()

    def list(self, file_path='ma_config.json'):
        try: # load values from configuration file
            with open(file_path) as file:
                config = json.load(file)
                if config['music_folder'] != "":
                    self._sMusicFolder = config['music_folder']
                else:
                    self._sMusicFolder = ".\Musics"
                self._lMusicPath = list(pathlib.Path(self._sMusicFolder).glob('*.mp3'))
                self._lMusicOrder = list(range(len(self._lMusicPath)))
                print(self._sMusicFolder)
                print(self._lMusicPath)
                print(self._lMusicOrder)
        except Exception as e: # use default values
            print(e)
            print('No music folder has been defined')
            print('\tHint: Set music_folder in ma_config.json file')
            #self._music_folder.set(filedialog.askdirectory())

    def length(self,_path):
        self._length = round(mixer.Sound(_path).get_length())
        print(self._length)


def play():
    mixer.music.play()

def stop():
    b_play = False
    mixer.music.stop()



if __name__ == '__main__':



    
    music = Music()
    mixer.init()

    # List the path from the config file / default musics
    music.list()
    
    # create tkinter
    music_player = tk.Tk()
    music_player.title("Music Player")
    music_player.geometry("500x420")

    # make playlist list
    playlist = tk.Listbox(music_player,fg = "navy", selectmode= tk.SINGLE)
    x = 0
    for i in music._lMusicPath:
        playlist.insert(x,i)
        x += 1
    print(playlist)

    _play_button = tk.Button(music_player, width = 5 , height= 3, text="Play", command= lambda: play(music) )#, command = music.toggleMusic())
    _stop_button = tk.Button(music_player, width = 5 , height= 3, text="Stop", command = stop)#, command = music.stop())
    #_forward_button = tk.Button(music_player, width = 5 , height= 3, text="Forward", command = music.toggleMusic())

    """
    var = tk.StringVar()
    var.set(playlist.get(tk.ACTIVE))
    song_title = tk.Label(music_player,textvariable = var)
    song_title.pack()
    """
    playlist.pack(fill="x")
    _play_button.pack(fill="x")
    _stop_button.pack(fill="x")


    music_player.mainloop()


    random.shuffle(music._lMusicOrder)

    for path in music._lMusicOrder:
        print(music._lMusicPath[path])
        mixer.music.load(music._lMusicPath[path])
        music.length(music._lMusicPath[path])
        #sound = mixer.music.load(f".\{path}")
        mixer.music.play()
        b_play = True

        _t_end = time.time() + music._length
        while time.time() < _t_end and b_play == True:
            pass
    # https://stackoverflow.com/questions/70483495/break-a-while-loop-when-a-button-is-pressed

    """
    while True:

            # test the functions    
        if get_sys()[0] == 1:
            print(get_sys()[1])
        else:
            print('ERROR')
            print(get_sys()[1]) 
            break


        
        music.list()
        music_list = list(pathlib.Path(music._music_folder).glob('*.mp3'))
        print(music_list)
        mixer.init()


        #mixer.music.load(f".\{music_list[0]}")
        #mixer.music.play()

        for path in music_list:
            mixer.music.load(f"{path}")
            music.length(path)
            #sound = mixer.music.load(f".\{path}")
            mixer.music.play()

            _t_end = time.time() + music._length
            while time.time() < _t_end:
                
                _user_input = input("Press p for Pause / Play or n for exit: ")

                if _user_input == 'n':
                    print("next song in in 2 sec..")
                    time.sleep(2)
                    break
                elif _user_input == 'p':
                    music.toggleMusic()
                elif _user_input == 's':
                    music.stop()
                    break
                else:
                    print("wrong input")
            
            if _user_input == 's':
                break

                

        _exit = input("Do you want to exit? (Y/N):")
        if _exit.lower() == 'y':
            break
        elif _exit.lower() == 'n':
            print("No exit - infinity run")

    """