# -*- coding: utf-8 -*-
"""hw3_carson_jenkins_ex_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WpI67_CZmhRrZ9w-JWVMUjitVtLFU3xJ
"""

'''
Homework 3, Exercise 1
Carson Jenkins
02/23/23
This program takes a given grid, and uses 
a for loop to print the grid out sideways.
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
  for j in range(len(grid)):
    print(grid[j][i], end='')
  print()