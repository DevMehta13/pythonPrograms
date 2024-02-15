# Program: To check if it's leap year or not.
# Author: Dev Mehta
# Date: 15th feb 2024.

def leap(year):
    if(year % 4 == 0):
        print("It is a leap year.")
    elif(year % 100 == 0 and year % 400 == 0):
        print("It is a leap year.")
    else:
        print("It is not a leap year.")

def main():
    year = int(input("Enter the year you want to check: "))
    leap(year)

if __name__ == "__main__":
    main()