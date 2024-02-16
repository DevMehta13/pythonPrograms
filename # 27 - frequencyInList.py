# Program: A program to count the frequency of elements in a list.
# Author: Dev Mehta
# Date: 16th feb 2024.

def count(arr):
    dict = {}

    for elem in arr:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1

    return dict

def main():

    arr = [int(x) for x in input("Enter the element of list with spaces: ").split()]

    frequencyDict = count(arr)

    print("The frequency of elements is: ")
    for key , value in frequencyDict.items():
        print(f"{key} - {value}")


if __name__ == "__main__":
    main()