import settings
from flask import Flask, render_template , request, redirect, url_for
import ma_music_player
import time

app = Flask(__name__) 

@app.route('/')
def index():
  # reading config values
  _l_config_values = settings.get_config(['wd_hour','wd_minute','we_hour','we_minute','music_limit','current_music','volume'])[1]
  return render_template('index.html', l_config_values = _l_config_values )  


@app.route('/next/')
def next():
  print("next music")
  settings.set_config(['music_status'],['next'])
  # after function redirect for index
  return redirect(url_for('index'))  

@app.route('/pause/')
def pause():
  print("music paused")
  settings.set_config(['music_status'],['pause'])
  # after function redirect for index
  return redirect(url_for('index')) 

@app.route('/unpause/')
def unpause():
  print("music unpaused")
  settings.set_config(['music_status'],['unpause'])
  # after function redirect for index
  return redirect(url_for('index'))  

@app.route('/stop/')
def stop():
  print("music stopped")
  settings.set_config(['music_status'],['stop'])
  # after function redirect for index
  return redirect(url_for('index'))  

@app.route('/update_alarm', methods =["GET", "POST"])
def update_alarm():
  if request.method == "POST":
      # getting inputs from HTML
      print(f'{request.form.get("wd_hour")}, {request.form.get("wd_minute")}, {request.form.get("we_hour")}, {request.form.get("we_minute")}, {request.form.get("music_limit")}, {request.form.get("volume_slider")}')
      _s_wd_hour = request.form.get("wd_hour")
      _s_wd_minute = request.form.get("wd_minute")
      _s_we_hour = request.form.get("we_hour")
      _s_we_minute = request.form.get("we_minute")
      _n_music_limit = int(request.form.get("music_limit"))
      _n_volume = int(request.form.get("volume_slider"))
      settings.set_config(['wd_hour','wd_minute','we_hour','we_minute','music_limit', 'volume'],[_s_wd_hour,_s_wd_minute,_s_we_hour,_s_we_minute,_n_music_limit,_n_volume])
  # after function redirect for index
  return redirect(url_for('index')) 


@app.route('/wd_on_off', methods =["GET", "POST"])
def wd_on_off():
  _l_wd_res = settings.get_config(['wd_hour','wd_minute'])[1]
  if _l_wd_res[0] == "-" or _l_wd_res[1] == "-" :
      _s_wd_hour = "09"
      _s_wd_minute = "00"
  else:
      _s_wd_hour = "-"
      _s_wd_minute = "-"

  settings.set_config(['wd_hour','wd_minute'],[_s_wd_hour,_s_wd_minute])
  # after function redirect for index
  return redirect(url_for('index')) 

@app.route('/we_on_off', methods =["GET", "POST"])
def we_on_off():
  _l_we_res = settings.get_config(['we_hour','we_minute'])[1]
  if _l_we_res[0] == "-" or _l_we_res[1] == "-" :
      _s_we_hour = "09"
      _s_we_minute = "00"
  else:
      _s_we_hour = "-"
      _s_we_minute = "-"

  settings.set_config(['we_hour','we_minute'],[_s_we_hour,_s_we_minute])
  # after function redirect for index
  return redirect(url_for('index')) 



if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0") # set it to TURE for debugging