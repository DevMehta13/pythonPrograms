# Program: To count number of words in a string.
# Author: Dev Mehta
# Date: 7th Aug 2023.
def numberOfWords(string) :
    words = string.split()# will split it into words.
    length = len(words)
    print("The number of words in the string is" , length)
def main() :
    string = str(input("Enter the string: " ))
    numberOfWords(string)
if __name__ == "__main__" :
    main()
