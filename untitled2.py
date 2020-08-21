# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:01:29 2020

@author: user
"""

import time, timeit

def clock(func):
    def clocked(*args):
        t0 = timeit.default_timer()
        result = func(*args)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
@clock

print("qqq")