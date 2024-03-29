from gevent import monkey
monkey.patch_all()
import gevent
import time
import json
import random
import requests
import sys

exper = json.loads(open(sys.argv[1], encoding='utf-8').read())

def send_request(i, time_):
    # print('send to', exper[i]['name'], time_, time.time())
    url = "http://0.0.0.0:5000/listen"
    action = exper[i]['name']
    requests.post(url, json = {"action_name": action, "params": {'runtime': exper[i]['runtime']}})

action_number = 388
one_minute = 60

def send_request_single_action(i, time_, total):
    if total == 0:
        return
    if time_ < total - 1:
        gevent.spawn_later(one_minute / total, send_request_single_action, i, time_ + 1, total)
    send_request(i, time_)
def send_memory_check(Minute, Second):
    url = "http://0.0.0.0:5000/load-info"
    requests.get(url, json={"time": Minute * 60 + Second})
    if(Second < 59):
        gevent.spawn_later(1, send_memory_check, Minute, Second + 1)
def run(time_):
    print('###################### time:', time_)
    send_memory_check(time_, 0)
    if time_ < 480 - 1:
        gevent.spawn_later(one_minute, run, time_ + 1)
    for i in range(action_number):
        total = int(exper[i]['invo'][time_])
        if total > 0:
            gevent.spawn_later(random.random() * (one_minute / total), send_request_single_action, i, 0, total)

run(0)
gevent.wait()
