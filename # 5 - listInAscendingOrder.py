def asc(inputList):
    sortedList = sorted(inputList)
    return sortedList

def main():
    numberOfElements = int(input('Enter the number of elements: '))
    myList = []
    for i in range(numberOfElements):
        element = int(input("Enter the element: "))
        myList.append(element)
    
    sortedList = asc(myList)  # Call the asc() function to sort the list
    
    print("Original list:", myList)
    print("Sorted list:", sortedList)

if __name__ == "__main__":
    main()
