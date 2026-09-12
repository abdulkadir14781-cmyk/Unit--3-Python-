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
n=int(input('Enter Number: '))
check_prime(n)