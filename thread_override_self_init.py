#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# def run(self):
#     """Method representing the thread's activity.
#     You may override this method in a subclass. The standard run() method
#     invokes the callable object passed to the object's constructor as the
#     target argument, if any, with sequential and keyword arguments taken
#     from the args and kwargs arguments, respectively.
#     """
#     try:
#         if self._target:
#             self._target(*self._args, **self._kwargs)
#     finally:
#         # Avoid a refcycle if the thread is running a function with
#         # an argument that has a member that points to the thread.
#         del self._target, self._args, self._kwargs

# def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs=None, *, daemon=None):
#         """This constructor should always be called with keyword arguments. Arguments are:
#         *group* should be None; reserved for future extension when a ThreadGroup
#         class is implemented.
#         *target* is the callable object to be invoked by the run()
#         method. Defaults to None, meaning nothing is called.
#         *name* is the thread name. By default, a unique name is constructed of
#         the form "Thread-N" where N is a small decimal number.
#         *args* is the argument tuple for the target invocation. Defaults to ().
#         *kwargs* is a dictionary of keyword arguments for the target
#         invocation. Defaults to {}.
#         If a subclass overrides the constructor, it must make sure to invoke
#         the base class constructor (Thread.__init__()) before doing anything
#         else to the thread.
#         """
#         assert group is None, "group argument must be None for now"
#         if kwargs is None:
#             kwargs = {}
#         self._target = target
#         self._name = str(name or _newname())
#         self._args = args
#         self._kwargs = kwargs
#         if daemon is not None:
#             self._daemonic = daemon
#         else:
#             self._daemonic = current_thread().daemon
#         self._ident = None
#         if _HAVE_THREAD_NATIVE_ID:
#             self._native_id = None
#         self._tstate_lock = None
#         self._started = Event()
#         self._is_stopped = False
#         self._initialized = True
#         # Copy of sys.stderr used by self._invoke_excepthook()
#         self._stderr = _sys.stderr
#         self._invoke_excepthook = _make_invoke_excepthook()
#         # For debugging and _after_fork()
#         _dangling.add(self)

import threading

class MyThread(threading.Thread):
    #overriding __init__ Method
    def __init__(self, number, function, arguments):
        #we have chosen our own parameters
        threading.Thread.__init__(self)
        self.number = number
        self.function = function
        self.arguments = arguments

    #overriding run method
    def run(self):
        print ('thread{} has started'.format(self.number))

        #from the original run method
        #self._target(*self._args, **self._kwargs)
        #they are self._target and passing the arguments onto them
        #so we did the same here
        self.function(*self.arguments)
        #  *self is there bcz arguments will be in the form of tuple or list

        print ('thread{} has finished'.format(self.number))

def multiplier(number, factor):
    for i in range(1,factor):
        number *= i
    print (number)

thread_list = []

for i in range (10):
    t = MyThread(number = i+1, function = multiplier, arguments = (i+1,5))
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()
