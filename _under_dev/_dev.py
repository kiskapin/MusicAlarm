import json
from pathlib import Path
from pygame import mixer
import time
import keyboard


def get_music_list(file_path='ma_config.json'):
    _result = 0
    with open(file_path) as file:
        config = json.load(file)
        _music_folder = config['music_folder']
        _result = 1
        return _result, _music_folder
    
    if _music_folder == '':
        return _result



def play_music(music):
    _result = 0 
    _mixer_status = 0
    try:
        mixer.init()
        #mixer.music.load(music)
        #mixer.music.play()
        m = mixer.Sound(music)
        m.play()
        print('Playing:' + music.stem)
        #print(mixer.music.get_length())
        while mixer.music.get_busy():
            _mixer_status = 1 
            if keyboard.read_key() == "s":
                print('Stop music')
                #mixer.pause()
                m.stop()
            if keyboard.read_key() == "p":
                print('Play music')
                #mixer.play()
                m.play()
            if keyboard.read_key() == "q":
                print('Quit music')
                #mixer.stop()
                m.stop()
            #time.sleep(60)

        print('mixer is NOT busy')
        time.sleep(2)
        _result = 1
        return _result

    except Exception as e:
        print(e)
        return _result


#class MusicPlayer(self, windows, music_folder):


if __name__ == '__main__':

    # get_music_list()
    test = get_music_list()
    print(test)
    _musics = [p for p in Path(test[1]).glob('*.mp3')]
    for x in _musics:
        print(x)
        play_music(x)