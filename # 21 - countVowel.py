# Program: To count each vowel
# Author: Dev Mehta
# Date: 15th feb 2024.

def vowel(word):
    length = len(word)
    a=0
    e=0
    i=0
    o=0
    u=0
    for j in range(0,length):
        if(word[j]=='a'):
            a = a + 1
        elif(word[j]=='e'):
            e = e + 1
        elif(word[j]=='i'):
            i = i + 1
        elif(word[j]=='o'):
            o = o + 1
        elif(word[j]=='u'):
            u = u + 1

    print("The number of a,e,i,o and u is " , a, " " , " " , e," " , i , " " , o ," " , "and" , u ,"respectively.")

def main():
    word = str(input("Enter the word: "))
    vowel(word)

if __name__ == "__main__":
    main()