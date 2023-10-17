'''
Homework 6, Exercise 2
Carson Jenkins
04/14/23
This program uses the cache decorator to save values in a function attribute
dictionary. Utilizing this should improve the runtime performance when
running something like the Fibonacci Sequence. Using the @cache decorator 
significantly improves the performance of the fibonacci function by 
avoiding redundant calculations.
'''

import functools

def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)
    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

def cache(func):
    @functools.wraps(func)
    def wrapperCache(*args, **kwargs):
        cacheKey = args + tuple(sorted(kwargs.items()))
        if cacheKey not in wrapperCache.cache:
            wrapperCache.cache[cacheKey] = func(*args, **kwargs)
        return wrapperCache.cache[cacheKey]
    wrapperCache.cache = {}
    return wrapperCache

@countCalls
@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))
print(fibonacci(16))