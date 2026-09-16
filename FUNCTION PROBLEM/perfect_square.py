def perfect_square(n):
    root=n**(0.5) 
    return root
n=int(input("num: "))    
result =perfect_square(n)
if result == int(result):
    print("perfect_square")
else:
    print("Not Perfect Square")    