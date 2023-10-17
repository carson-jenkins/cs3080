'''
Homework 6, Exercise 1
Carson Jenkins
04/14/23
This program uses the function slowDown which sleeps for a second before calling the
decorated function. 
'''

import time

def slow_down(rate=1):
  def decorator(value):
    def wrapper(*args, **kwargs):
      time.sleep(rate)
      return value(*args, **kwargs)
    return wrapper
  return decorator

@slow_down()
def countdown(fromNumber):
  if fromNumber < 1:
    print("0")
  else:
    print(fromNumber)
    countdown(fromNumber - 1)

countdown(5)