#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importing threading module
import threading
#importing time module
import time

def func(name):
    print ("Hi,its {}\n".format(t.name),end="")
    time.sleep(3)
    print ("{} is now active".format(name))



threads_list = []

start = time.time()

for i in range(5):
    t = threading.Thread(target = func, name = 'thread{}'.format(i+1), args = ('thread{}'.format(i+1),))
    threads_list.append(t)
    t.start()
    print ("{} has started".format(t.name))

for t in threads_list:
    t.join()

end = time.time()

print ("time taken: {}".format(end-start))

print ("all live threads finished job")
