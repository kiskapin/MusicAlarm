import settings
from flask import Flask, render_template , request
import ma_music_player
import time

app = Flask(__name__)

@app.route('/')
def index():
  # reading current alarm times
  _l_alarm_times = settings.get_config(['wd_hour','wd_minute','we_hour','we_minute'])[1]
  return render_template('index.html', l_alarm_times = _l_alarm_times )


@app.route('/next/')
def next():
  print("next music")
  ma_music_player.set_status("next")
  time.sleep(0.48)
  ma_music_player.set_status()
  # reading current alarm times
  _l_alarm_times = settings.get_config(['wd_hour','wd_minute','we_hour','we_minute'])[1]
  return render_template('index.html', l_alarm_times = _l_alarm_times )

@app.route('/pause/')
def pause():
  print("music paused")
  ma_music_player.set_status("pause")
  # reading current alarm times
  _l_alarm_times = settings.get_config(['wd_hour','wd_minute','we_hour','we_minute'])[1]
  return render_template('index.html', l_alarm_times = _l_alarm_times )  

@app.route('/unpause/')
def unpause():
  print("music unpaused")
  ma_music_player.set_status("unpause")
  # reading current alarm times
  _l_alarm_times = settings.get_config(['wd_hour','wd_minute','we_hour','we_minute'])[1]
  return render_template('index.html', l_alarm_times = _l_alarm_times )  

@app.route('/stop/')
def stop():
  print("music stopped")
  ma_music_player.set_status("stop")
  # reading current alarm times
  _l_alarm_times = settings.get_config(['wd_hour','wd_minute','we_hour','we_minute'])[1]
  return render_template('index.html', l_alarm_times = _l_alarm_times )  

@app.route('/update_alarm', methods =["GET", "POST"])
def update_alarm():
    if request.method == "POST":
       # getting inputs from HTML
       _n_wd_hour = request.form.get("wd_hour")
       _n_wd_minute = request.form.get("wd_minute")
       _n_we_hour = request.form.get("we_hour")
       _n_we_minute = request.form.get("we_minute")
       #return (f"we: {_n_wd_hour}{_n_wd_minute} wd: {_n_we_hour}{_n_we_minute}")
       settings.set_config(['wd_hour','wd_minute','we_hour','we_minute'],[_n_wd_hour,_n_wd_minute,_n_we_hour,_n_we_minute])
       
    # reading current alarm times
    _l_alarm_times = settings.get_config(['wd_hour','wd_minute','we_hour','we_minute'])[1]
    return render_template('index.html', l_alarm_times = _l_alarm_times )  



if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0") # set it to TURE for debugging