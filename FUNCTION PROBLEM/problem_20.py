import math
def find_factorial(n):
    fact=math.factorial(n)
    print(f"Factorial:{fact}")

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

def check_even_odd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
        
def input_number():
    n=int(input('Enter number: '))
    check_even_odd(n)
    check_prime(n)
    find_factorial(n)
input_number()