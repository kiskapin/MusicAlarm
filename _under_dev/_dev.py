import json
import pathlib
from pygame import mixer
import time
import keyboard
import random


class Music():

    def __init__(self):
        self.IsPaused = False
        self._music_folder = '.\Musics'
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
                self._music_folder = config['music_folder']
                print(self._music_folder)
        except Exception as e: # use default values
            print(e)
            print('No music folder has been defined')
            print('\tHint: Set music_folder in ma_config.json file')
            #self._music_folder.set(filedialog.askdirectory())

    def length(self,_path):
        self._length = round(mixer.Sound(_path).get_length())
        print(self._length)


if __name__ == '__main__':

    music = Music()
    mixer.init()

    # List the path from the config file / default musics
    music.list()
    music_list = list(pathlib.Path(music._music_folder).glob('*.mp3'))
    print(music_list)

    play_order = list(range(1,len(music_list)+1))
    random.shuffle(play_order)
    print(play_order)
