def add(a,b):
    print(f"Addition: {a+b}")
def subtract(a,b):
    print(f"Subtraction:{a-b}")
def multiply(a,b):
    print(f"Multiplication:{a*b}")
def division(a,b):
    print(f"Division:{a/b}")
while True:
    a=int(input('Ener number: '))
    b=int(input('Ener number: '))
    choice=input('Enter opertion: ').lower()

    if choice=="+":
        add(a,b)
    elif choice=="-":
        subtract(a,b)
    elif choice=="*":
        multiply(a,b)
    elif choice=="/":
        division(a,b)
    elif choice=="exit":
        break
    else:
        print("invalid Choice")