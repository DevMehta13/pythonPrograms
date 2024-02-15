# Program: To merge two dictionaries.
# Author: Dev Mehta
# Date: 15th feb 2024.

def mergeDictionaryApproach1(dict1,dict2):
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    merged_dict.update(dict2)  # Update it with the second dictionary
    return merged_dict

def mergeDictionaryApproach2(dict1,dict2):
    return { **dict1,**dict2 } # This ** is used to unpack the dictionary

def main():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}

    merged_dict = mergeDictionaryApproach1(dict1, dict2) # can do with any approach
    print("Merged dictionary:", merged_dict)

if __name__ == "__main__":
    main()