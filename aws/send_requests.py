from gevent import monkey
monkey.patch_all()
import gevent
import time
import json
import random
import requests
import sys

filename = sys.argv[1]
wf = json.loads(open(filename, encoding='utf-8').read())
invos = {}
for app in wf:
    invos[app] = wf[app]['invo']


c1, c2 = {}, {}


def send_func(action, runtime):
    #print('send to', action, runtime)
    url = "http://0.0.0.0:5000/listen"

    if action not in c1:
        c1[action] = 1
        c2[action] = 0
    else:
        c1[action] += 1
    # print('come:', action, c1[action], c2[action])

    requests.post(url, json = {"action_name": action, "params": {'runtime': runtime}})

    c2[action] += 1
    
def send_app(app):
    functions = wf[app]['functions']
    for func in functions:
        start_time = float(functions[func]['start_time'])
        runtime = float(functions[func]['duration'])
        gevent.spawn_later(start_time, send_func, func, runtime)
        
def send_single_app(app, time_, total):
    if time_ < total - 1:
        gevent.spawn_later(1 / total, send_single_app, app, time_ + 1, total)
    send_app(app)

def run(time_):
    total_time = 7200
    print('###################### time:', time_)
    if time_ < total_time - 1:
        url = "http://0.0.0.0:5000/load-info"
        requests.get(url, json={"time": time_})  # 每隔1s进行一次内存信息访问请求
        gevent.spawn_later(1, run, time_ + 1)
    for app in invos:
        total = invos[app][time_]
        if total > 0:
            gevent.spawn_later(random.random() * (1.0 / total), send_single_app, app, 0, total)
   
run(0)
gevent.wait(timeout = 7400)
