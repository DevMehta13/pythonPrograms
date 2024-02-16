# Program: A program to generate a random number.
# Author: Dev Mehta
# Date: 16th Feb 2024.

import random

def generate_random_number(start, end):
    return random.randint(start, end) # This is a function to give random number between start and end.

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    random_number = generate_random_number(start, end)
    
    print("Random number between", start, "and", end, ":", random_number)

if __name__ == "__main__":
    main()
