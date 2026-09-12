def fact(n):
    product=1
    i=1
    while i<=n:
        product=product*i
        i+=1
    return product
n=int(input('Enter Number: '))
print(f"Factorial: {fact(n)}")
