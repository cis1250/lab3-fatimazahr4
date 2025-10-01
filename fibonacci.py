#!/usr/bin/env python3
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
while True:
    try:
# Prompt the user for the number of terms.
        n = int(input("Enter the number of terms: "))
# Validate that the input is a positive integer.
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        else:
              break #exit loop
    except ValueError:
        print("Please enter a positive integer.")
    
# Use a for loop to print the Fibonacci sequence up to that many terms.
a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # newline


