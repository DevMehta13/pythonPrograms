def binary(number):
  remiander = ""
  while(number > 0):
      remainder = str(number % 2) + remainder
      number = number // 2
  print("The binary number is: " + remainder)

def main():
  number = int(input("Enter a number: "))
  binary(number)

if __name__ == "__main__":
  main()
