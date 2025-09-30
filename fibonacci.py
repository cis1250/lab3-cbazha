#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

fib = input("How many terms of the fibonacci sequence do you want?")

if (int(fib)<=0):
  input("Please enter a positive integer.")
else:
  x = 0
  y = 1
  num = 0
  
  for num in range(int(fib)):
    x, y = y, x + y
    print(x)
