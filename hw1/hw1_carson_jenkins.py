'''
Homework 1
Carson Jenkins
02/02/23
This is a security program that runs through a series of questions, 
restarting the loop each time the user is incorrect, and revealing a 
secret after the user successfully answers all the questions in a row.
'''
import random
incorrect = "Incorrect, start over"
correct = "Correct, continue"
# Initializing restart variable as false with a "Falsey" value
restart = ""
# "Truthy" value used for while loop
while 1:
  # Prompts user for side, and has them calculate area of either 
  # a square or triangle, restarts while loop if incorrect
  while 1:
    print("1. Square\n2. Triangle\n")
    area_choice = input("Which do you want the area for? ")
    if area_choice == str(1):
      side = input("Length of side: ")
      area = int(side) * int(side)
      area_answer = input("Compute area of square with side length " + str(side) + ": ")
      if int(area_answer) != area:
        print(incorrect)
        continue
      break
    elif area_choice == str(2):
      base = input("Base of triangle: ")
      height = input("Height of triangle: ")
      # Float value used here
      area = 0.5 * int(base) * int(height)
      area_answer = input("Compute area of trangle with base " + str(base) + " and height " + str(height) + ": ")
      if int(area_answer) != area:
        print(incorrect)
        continue
      break
    else:
      print("Error: enter either 1 or 2")
  # This for loop repeats 3 times, prompting the user with randomly 
  # generated equations. The second number is provided by the index, 
  # which is based on the randomized range values. 3 different 
  # operators are used based on index
  rand_range = random.randint(1, 20)
  for i in range(rand_range, rand_range+3):
    first_number = random.randint(50, 100)
    if i == rand_range:
      mod_answer = input(str(first_number) + " % " + str(i) + " = ")
      correct = first_number % (i)
    elif i == rand_range + 1:
      mod_answer = input(str(first_number) + " - " + str(i) + " = ")
      correct = first_number - (i)
    else:
      print("Disregard decimal remainder: ")
      mod_answer = input(str(first_number) + " // " + str(i) + " = ")
      correct = first_number // (i)
    if int(mod_answer) != correct:
      print(incorrect)
      restart = True
      break
    else:
      print(correct)
  # Restarts the while loop if any answers were incorrect in the for loop
  if restart:
    continue
  break
# Last section displays secret passwords the program is leading you to unlock
secrets = ["jdajs998fd", "34neJnf34", "pswd145unlck23", "013003Uo"]
print("You completed the security quiz. Here are all of your passwords: ")
for i in range(len(secrets)):
  print(secrets[i])
