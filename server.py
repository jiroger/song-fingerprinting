from flask import Flask, render_template, url_for
from flask_ask import Ask, statement, question
import requests
import time
import unidecode
import json
from SongFingerPrinting import SongFingerPrinting as fp
from flask import request

app = Flask(__name__)
ask = Ask(app, '/')

songfp = fp()
songfp.example_load()

@app.route('/')
def index():
    return render_template('template.html', msg = "Please enter the length of the excerpt", url = "", songcount = len(songfp.songnames))

@app.route('/start/', methods = ['POST'])
def start():
    time = request.form.get("length", None)
    if type(time) is None or time == "" or int(time) < 0:
        return render_template('template.html', msg="Please enter a valid input greater than 0", url="..", songcount = len(songfp.songnames))
    
    time = int(time)
        
    song = songfp.make_excerpt(time)
    out = songfp.match_song(song)
    
    return render_template('start.html', out = out, time = time)

@app.route('/stop/')
def stop():
    return render_template('stop.html')

if __name__ == '__main__':
    app.run(debug=True)