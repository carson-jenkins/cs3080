# -*- coding: utf-8 -*-
"""hw4_carson_jenkins_ex_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kVoiLGBETrCO-rIR3lJGgUAsDmFd9bME
"""

'''
Homework 4, Exercise 3
Carson Jenkins
03/09/23
This program checks input for a strong password, checking for at least 8 
characters, at least one upper and lower case letter, and at least one digit.
'''

import re

# (?=.{8,}) - checks for at least 8 characters
# (?=.*[a-z]) - checks upper case
# (?=.*[A-Z]) - checks lower case
# (?=.*\d) - checks for a digit
requirement = re.compile("(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*\d)")

# reads password from user
password = input("Enter password: ")

# checks password with the requirement
strong = re.search(requirement, password)

if strong:
  print("Password is strong")
else:
  print("Password is weak")