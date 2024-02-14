def power(base , exponent):
    if(exponent==0):
        return 1
    else:
        return base*power(base,exponent-1)
    
def main():
    base = float(input("Enter the value of base: "))
    exponent = float(input("Entere the value of exponent: "))

    result = power(base,exponent)

    print("result is " , result)

if __name__ == "__main__":
    main()