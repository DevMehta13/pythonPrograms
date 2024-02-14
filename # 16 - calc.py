def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if(y==0):
        print("Invalid input for this operation.")
    else:
        return x//y


def main():
    num1 = float(input("Enter the number 1: "))
    num2 = float(input("Enter the number 2: "))

    print("Addition: " , add(num1,num2))
    print("Subtraction: " , sub(num1,num2))
    print("Multiplication: " , multiplication(num1,num2))
    print("Division: " , division(num1,num2))

if __name__ == "__main__":
    main()