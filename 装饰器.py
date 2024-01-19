from datetime import datetime


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


import time
import functools


def decorator(func):
    def wrapper(*args, **kw):
        print('begin call')
        result = func(*args, **kw)
        print('end call')
        return result

    return wrapper


# @log
@decorator
def now():
    print(datetime.now())


now()
