# Program: To find roots of quadratic equation.
# Author: Dev Mehta
# Date: 14th feb 2024.

import math

def find_roots(a, b, c):
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    
    else:
        return "No real roots"

def main():
    
    a = float(input("Enter the coefficient of x^2: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant term: "))

    roots = find_roots(a, b, c)
    print("Roots:", roots)

if __name__ == "__main__":
    main()