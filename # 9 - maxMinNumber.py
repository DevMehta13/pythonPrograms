# Program: To find maximum and minimum number in a list.
# Author: Dev Mehta
# Date: 7th Aug 2023.
def swap(x,y) :
    t = x
    x = y
    y = t
def maximum(list,size) :
    max = list[0]
    for i in range (1,size) :
        if( list[i] > max) :
            max = list[i]
        else :
            max = max
    print("The maximum value in list is " , max)
def minimum(list,size) :
    min = list[0]
    for i in range (1,size) :
        if( list[i] < min) :
            min = list[i]
        else :
            min = min
    print("The minimum value in list is " , min)
def main() :
    size = int(input("Enter the size of list: "))
    list = []
    for i in range (0,(size)) :
        element = int(input("Enter the element: "))
        list.append(element)
    maximum(list,size)
    minimum(list,size)
if __name__ == "__main__" :
    main() 