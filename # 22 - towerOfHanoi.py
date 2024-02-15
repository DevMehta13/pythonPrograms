# Program: To solve tower of hanoi problem.
# Author: Dev Mehta
# Date: 15th feb 2024.

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

def main():
    n = int(input("Enter the number of disks: "))
    tower_of_hanoi(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()
