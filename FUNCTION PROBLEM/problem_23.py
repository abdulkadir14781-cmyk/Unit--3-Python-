def display(a,b):
    print(f"Square:{a}\nCube:{b}")

def cube(n):
    return n**3

def square(n):
    return n**2
    
def get_number():
    n=int(input('Enter Number: '))
    result1=square(n)
    result2=cube(n)
    display(result1,result2)
get_number()