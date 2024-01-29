def primeno(n):
  prime = 0
  for i in range(2 , n):
    for j in range(2 , i):
      if (i%j == 0):
          prime = 0
          break
      else:
          prime = 1
    if(prime == 1):
      print(i)
def main():
  a = int(input("Enter the number: "))
  primeno(a)
if __name__ == "__main__" :
  main() 
