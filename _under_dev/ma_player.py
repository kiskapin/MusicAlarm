from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    def __init__(self, win):
        # Create Tkinter window
        win.geometry('200x200')
        win.title('Music Player')
        win.resizable(0, 0)

        # StringVar to change button text later
        self.play_restart   = tk.StringVar()
        self.pause_resume   = tk.StringVar()
        self._music_folder  = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        # The buttons and their positions
        #load_button = Button(win, text='Load', width=10, font=('Arial', 16), command=self.load)
        #load_button.place(x=100, y=40, anchor='center')

        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 16), command=self.play)
        play_button.place(x=100, y=80, anchor='center')

        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 16), command=self.pause)
        pause_button.place(x=100, y=120, anchor='center')

        stop_button = Button(win, text='Stop', width=10, font=('Arial', 16), command=self.stop)
        stop_button.place(x=100, y=160, anchor='center')

        self.music_file = False
        self.playing_state = False

    def load(self):
        try: # load values from configuration file
            self.get_music_list()
        except: # use default values
            print('No music folder has been defined')
            self._music_folder.set(filedialog.askdirectory())

        print("Loaded: ", self._music_folder)
        self.play_restart.set('Play')

    def play(self):
        if self._music_folder:
            for self.music_file in self._music_folder:
                mixer.init()
                mixer.music.load(str(self.music_file))
                mixer.music.play()
            
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    def stop(self):
        mixer.music.stop()


    def get_music_list(self, file_path='ma_config.json'):
        with open(file_path) as file:
            config = json.load(file)
            self._music_folder.set(config['music_folder'])
    

if __name__=='__main__':
    """
    root = Tk()
    MusicPlayer(root)
    root.mainloop()
    """

