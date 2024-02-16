# Program: To get input in dictionaries.
# Author: Dev Mehta
# Date: 16th feb 2024.

def inputDict():
    dict = {}
    while True:
        keyValue = input("Enter the key and value in format ' key:value ' and press enter when you are finished: ")
        if keyValue == "":
            break
        key , value = keyValue.split(":")
        dict[key.strip()] = value.strip()

    return dict

def main():
    print("Enter the key-value pairs for dictionary: ")

    dict1 = inputDict()

if __name__ == "__main__":
    main()