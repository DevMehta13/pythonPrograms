# Program: To reverse a string.
# Author: Dev Mehta
# Date: 7th Aug 2023.
def reverse(string) :
    string1 = str(string[::-1])
    print("The reverse of entered string is " , string1)
def main() :
    string = str(input("Enter the string: "))
    reverse(string)
if __name__ == "__main__" :
    main()