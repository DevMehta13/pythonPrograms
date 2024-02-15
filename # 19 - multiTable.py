# Program: To write multiplication table of a number
# Author: Dev Mehta
# Date: 15th feb 2024.

def multi(number):
    print("The multiplication table of " , number , "is:\n")
    for i in range(1,11):
        print(number , " * " , i , " = " , number*i , "\n")

def main():
    number = int(input("Enter the number: "))
    multi(number)

if __name__ == "__main__":
    main()