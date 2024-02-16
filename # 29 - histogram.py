# Program: A program to create a histogram from a list of integers.
# Author: Dev Mehta
# Date: 16th feb 2024.

import matplotlib.pyplot as plt

def create_histogram(data):
    plt.hist(data, bins=10, edgecolor='black')  # Create histogram with 10 bins
    plt.xlabel('Value')  # Label for x-axis
    plt.ylabel('Frequency')  # Label for y-axis
    plt.title('Histogram of Integers')  # Title of the histogram
    plt.grid(True)  # Add grid lines
    plt.show()  # Display the histogram

def main():
    # Input list of integers from the user
    data = [int(x) for x in input("Enter a list of integers separated by space: ").split()]

    # Create histogram from the input data
    create_histogram(data)

if __name__ == "__main__":
    main()
