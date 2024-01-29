def primeno(n):
    prime = 0
    for i in range(2 , n):
        if (n%i == 0):
            prime = 0
            break
        else:
            prime = 1
    if(prime == 0):
        print("it is not a prime number.")
    else:
        print("it is a prime number.")
def main():
    a = int(input("Enter the number: "))
    primeno(a)
if __name__ == "__main__" :
    main() 
        
    
