#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time

count = 5

def func1():
    global count
    while True:
        if count == 1000:
            break
        print ('count : {}'.format(count))
        count+=1
        time.sleep(2)

def func2():
    global count
    for i in range(1,10):
        count+=i
        time.sleep(1)

t1 = threading.Thread(target = func1, name = 'Thread1', daemon = True)
t2 = threading.Thread(target = func2, name = 'Thread2')

t1.start()
t2.start()

t2.join()

print ("End value of count: {}".format(count))
