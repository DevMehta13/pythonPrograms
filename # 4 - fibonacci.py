number = int(input('Enter the number: '))
firstTerm = 0
secondTerm = 1
count = 0
if number<=0 : 
    print("Enter the positive value")
elif number == 1 :
    print(firstTerm)
else :
    print("Fibonacci sequence: \n")
    print(firstTerm)
    while count < number : 
        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm
        count += 1