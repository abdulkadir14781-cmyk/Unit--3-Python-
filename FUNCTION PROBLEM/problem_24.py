import math
def find_square(n):
    print(f"Square:{n**2}")
    
def find_factorial(n):
    print(f"Factorial:{math.factorial(n)}")

def check_even_odd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

def check_prime(n):
    if n<=1:
        print("Not Prime")
    else:
        for i in range(2,n):
            if n%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")

while True:
    print("1.Check Even/Odd\n2.Check Prime\n3.Find Factorial\n4.Find Square\n5.Exit")
    n=int(input('Enter Number: '))
    choice=int(input('Enter choice: '))

    if choice==1:
        check_even_odd(n)
    elif choice==2:
        check_prime(n)
    elif choice==3:
        find_factorial(n)
    elif choice==4:
        find_square(n)
    elif choice==5:
        break
    else:
        print("Invalid Choice")

    