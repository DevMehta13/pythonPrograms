# Program: A program to perform a binary search on a list of numbers.
# Author: Dev Mehta
# Date: 15th feb 2024.

def binary(arr,target):
    start = 0 
    end = len(arr) - 1

    while(start<=end):
        mid = (start+end) // 2

        if(arr[mid]==target):
            return mid
        
        elif(arr[mid]<target):
            start = mid + 1

        else:
            end = mid - 1

    return -1

def main():
    arr = sorted([int(x) for x in input("Enter the sorted list's number with spaces: ").split()])

    target = int(input("Enter the number you want to search in the list: "))

    index = binary(arr,target) 

    if(index != -1):
        print(f"The {target} is present at {index} index in the list.")
    
    else:
        print(f"The {target} is not in your list.")

if __name__ == "__main__":
    main()