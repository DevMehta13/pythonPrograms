# Program: A program to check if a substring is present in a given string.
# Author: Dev Mehta
# Date: 16th feb 2024.

def subStringInString(string , substring):
    if substring in string:
        return 1
    else:
        return 0
    
def main():
    string = str(input("Enter the string: "))
    subString = str(input("Enter the substring you want to find in string: "))

    if subStringInString(string,subString):
        print("The substring exist in the string.")
    else:
        print("The substring does not exist in the string.")


if __name__ == "__main__":
    main()