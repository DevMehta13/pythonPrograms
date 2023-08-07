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