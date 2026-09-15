def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum        
n=int(input("num= "))            
result = perfect_num(n)        
if result == n:
    print("perfect ")        
else:
    print("Not perfect ")
      