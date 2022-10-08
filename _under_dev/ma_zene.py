import os
import sys
from pygame import mixer
# importing time module
import time

"""
def play_music(path):

    print(path)
    _songs = [p for p in Path(f"{path}").glob('*.mp3')]
    for song in _songs:
        # creating vlc media player object
        media_player = vlc.MediaPlayer()
        # media object
        media = vlc.Media(f"{song}")
        # setting media to the media player
        media_player.set_media(media)
        # setting volume
        media_player.audio_set_volume(70)
        # setting video scale
        media_player.video_set_scale(0.6)
        # setting audio track
        media_player.audio_set_track(1)
        # start playing video
        media_player.play()
        # wait so the video can be played for 5 seconds
        # irrespective for length of video
        time.sleep(50)
        #os.system('\Lonely.mp3')


#def vlc():

"""

"""
class Player():
    def __init__(self, **kwargs):
        # Shared Variable.
        #self.status = {}
        self.play = True
    
"""

if __name__ == '__main__':
    
    #play_music(r'C:\Personal\Projects\DEV\MusicAlarm\Musics')
    p = (r'C:\Personal\Projects\DEV\MusicAlarm\Musics\Lonely.mp3')

    mixer.init()
    mixer.music.load(p)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)