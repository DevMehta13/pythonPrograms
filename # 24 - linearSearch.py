# Program: A program to perform a linear search on a list of numbers.
# Author: Dev Mehta
# Date: 15th feb 2024.

def linear(arr,target):
    for i in range(0,len(arr)):
        if(arr[i] == target):
            return i
    return 0

def main():
    arr = [int(x) for x in input("Enter the numbers in list with space: ").split()]

    target = int(input("Enter the number whose position you want to find: "))

    result = linear(arr,target)

    if(result != 0):
        print(f"The {target} is present at index {result}.")
    else:
        print(f"The target is not in the list.")

if __name__ == "__main__":
    main()