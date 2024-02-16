# Program: A program to find the sum of sine series up to n terms.
# Author: Dev Mehta
# Date: 16th Feb 2024.

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def sine(x, n):
    sum = 0
    for i in range(n):
        sum += ((-1) ** i) * (x ** (2 * i + 1)) / fact(2 * i + 1)
    return sum

def main():
    x = float(input("Enter the angle: "))
    n = int(input("Enter the terms up to which the sum of sine series is required: "))

    result = sine(x, n)

    print(f"The sum of sine series up to {n} terms is {result}.")

if __name__ == "__main__":
    main()
