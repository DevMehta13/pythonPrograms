# Program: To swap two numbers
# Author: Dev Mehta
# Date: 14th feb 2024.

def swap(num1, num2):
    return num2, num1  # Return the swapped values

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("Before swapping: ", num1, " ", num2)

    num1, num2 = swap(num1, num2)  # Assign the swapped values back to num1 and num2

    print("After swapping: ", num1, " ", num2)    

if __name__ == "__main__":
    main()
