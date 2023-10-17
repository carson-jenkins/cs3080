'''
Homework 5, Exercise 1
Carson Jenkins
03/22/2023
This program creates an iterator class called ReverseIter,
it takes a list and iterates it from the reverse direction.
'''

# takes a list and iterates it in the reverse direction
class ReverseIter:
  def __init__(self, itList):
    self.itList = itList
    self.position = len(itList)
        
  def __iter__(self):
    return self
        
  def __next__(self):
    if self.position <= 0:
      # return None to stop the iterator
      return None
    self.position -= 1
    # return index of iterator list
    return self.itList[self.position]
        
it = ReverseIter([1, 2, 3, 4])
for num in it:
  if num is None:
    break
  print(num)