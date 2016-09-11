# -*- coding: utf-8 -*-
import argparse
import sys
import os
import socket
import datetime
import time
import threading
try:
    import Queue
except ImportError:
    import queue as Queue
from discosub.core.ui import info, success, fail
import discosub

results = []
BASE_PATH = os.path.dirname(discosub.__file__)

def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


class Worker(threading.Thread):

    def __init__(self, queue, name):
        threading.Thread.__init__(self)
        self._queue = queue
        self.name = name

    def run(self):
        while True:
            # queue.get() blocks the current thread until
            # an item is retrieved.
            msg = self._queue.get()

            if isinstance(msg, str) and msg == 'quit':
                # if so, exists the loop
                break
            try:
                print("testing: {0}".format(msg))
                ip = socket.gethostbyname(msg)
                result = '{0} => {1}'.format(msg, ip)
                results.append(result)
            except socket.gaierror:
                continue


def thats_all_folks(start):
    end = datetime.datetime.now()
    hours, minutes, seconds = convert_timedelta(end - start)
    print("Ending at {0}\n".format(end))
    print("{0} results find in {1} hours {2} minutes {3} seconds".format(
        len(results), hours, minutes, seconds))
    print("Results:")
    for result in results:
        print(result)


def analyze(target, agressive):
    start = datetime.datetime.now()
    subdomains = []

    keywords_file = os.path.join(BASE_PATH, "dictionaries", "essential.py")
    if agressive:
        keywords_file = os.path.join(BASE_PATH, "dictionaries", "agressive.py")
    with open(keywords_file) as myDictionary:
        subdomains = myDictionary.readlines()

    print("We have {0} possibilities".format(len(subdomains)))
    print("Starting at {0}\n".format(start))

    queue = Queue.Queue()
    workers = []
    max_worker = 30
    if agressive:
        max_worker = 400
    for index in range(0, max_worker):
        worker = Worker(queue, "worker{0}".format(index))
        worker.start()
        workers.append(worker)

    [queue.put("{0}.{1}".format(sub.replace("\n", ""), target)) for sub in subdomains]
    [queue.put("quit") for worker in workers]

    for worker in workers:
        worker.join()

    thats_all_folks(start)
