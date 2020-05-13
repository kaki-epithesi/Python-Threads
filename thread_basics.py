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

#t is a thread for the function "func" , it has mainly 3
#parameters , 1st parameter is the target function,
#2nd parameter is the name of the thread
#3rd parameter is the args of the function in the form of a tuple

t = threading.Thread(target = func, name = 'Thread1', args = ("Thread1",))

#start() function starts the thread

t.start()

# t.join()
#
# threads_list = []
#
# start = time.time()
#
# for i in range(5):
#     t = threading.Thread(target = func, name = 'thread{}'.format(i+1), args = ('thread{}'.format(i+1),))
#     threads_list.append(t)
#     t.start()
#     print ("{} has started".format(t.name))
#
# for t in threads_list:
#     t.join()
#
# end = time.time()
#
# print ("time taken: {}".format(end-start))
#
# print ("all live threads finished job")
