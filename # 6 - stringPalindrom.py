# Program: To check if string is palindrome or not.
# Author: Dev Mehta
# Date: 7th Aug 2023.
def palindrome(string) :
    string = string.lower()#convert every alphabet to lowercase so there is no confusion.
    if string == string[::-1] :#string[::-1] koi bhi word ko ulta kar dega jaise dev ko ved kar dega.
        print(string , " is a palindrome string.")
    else : 
        print(string , " is not a palindrome string.")
def main() : 
    string = str(input("Enter the word: "))
    palindrome(string)
if __name__ == "__main__" :
    main()
