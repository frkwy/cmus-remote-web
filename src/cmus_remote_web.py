from bottle import route, run
from now_playing import now_playing
import os

@route('/cmus/next')
def next():
    os.system("cmus-remote -n")
    return "next!"

@route('/cmus/pause')
def pause():
    os.system("cmus-remote -u")
    return "success"

@route('/cmus/shuffle')
def shuffle():
    os.system("cmus-remote -s")
    return "success"

@route('/')
def top():
    return now_playing()

run(host='0.0.0.0', port=5000)
