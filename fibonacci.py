#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

fib = input("How many terms of the fibonacci sequence do you want?")

while (int(fib)<=0):
  input("Please enter a positive integer.")
x = 0
y = 1

for num in fib:
  x = fib
  y = fib + x
  print(x, y)
