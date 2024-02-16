# Program: A program to find the ASCII value of a character.
# Author: Dev Mehta
# Date: 16th feb 2024.


def main():
    character = str(input("Enter the character whose ASCII value is required: "))

    asciiValue = ord(character) #It is an in built function in python to get ascii value.

    print(f"The ASCII value of {character} is {asciiValue}.")

if __name__ == "__main__":
    main()
