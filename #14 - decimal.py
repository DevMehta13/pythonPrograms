def binary_to_decimal(n):
    decimal_num = 0
    power = 0
    while(n > 0):
        decimal_num += (n % 10) * (2**power)
        n = n // 10
        power += 1
    print("The decimal number is: " + str(decimal_num))

def main():
    number = int(input("Enter a binary number: "))
    binary_to_decimal(number)

if __name__ == "__main__":
    main()
