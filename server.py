import settings
from flask import Flask, render_template , request
import ma_music_player
import time

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/next/')
def next():
  print("next music")
  ma_music_player.set_status("next")
  time.sleep(0.48)
  ma_music_player.set_status()
  return render_template('index.html')

@app.route('/pause/')
def pause():
  print("music paused")
  ma_music_player.set_status("pause")
  return render_template('index.html')

@app.route('/unpause/')
def unpause():
  print("music unpaused")
  ma_music_player.set_status("unpause")
  return render_template('index.html')

@app.route('/stop/')
def stop():
  print("music stopped")
  ma_music_player.set_status("stop")
  return render_template('index.html')



if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0") # set it to TURE for debugging