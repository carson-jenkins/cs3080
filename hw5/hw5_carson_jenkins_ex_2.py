'''
Homework 5, Exercise 2
Carson Jenkins
03/22/2023
This program finds the first n Pythagorean triplets. It's a 
triplet if x*x + y*y = z*z, where x, y, and z are all integers.
'''

def pyt(n):
  triplets = []
  for z in range(1, n+1):
    for y in range(1, z):
      for x in range(1, y):
        if x*x + y*y == z*z:
          triplets.append((x, y, z))
  # returns a list of triplets instead of a generator object
  return triplets

# to get the first n triplets, the take function is used
def take(n, seq):
  # return first n items in the sequence seq as a list
  return [seq[i] for i in range(n)]

print(take(10, pyt(30)))