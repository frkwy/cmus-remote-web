from bottle import route, run
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

run(host='0.0.0.0', port=5000)
