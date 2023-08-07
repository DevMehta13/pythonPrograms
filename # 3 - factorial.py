# Program: To get factorial of enterd number.
# Author: Dev Mehta
# Date: 7th Aug 2023.
number = int(input('Enter the number whose factorial you want to find: ' ))
factorial = 1
if number < 0 : 
    print("The factorial of ",number," does not exist.")
elif number == 0 :
    print("The factorial of ",number," is 1.")
else :
    for i in range(1,number+1) :
        factorial *= i
print("The factorial of ",number," is ",factorial)
