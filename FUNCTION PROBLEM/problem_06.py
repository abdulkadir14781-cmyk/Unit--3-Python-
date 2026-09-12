def calculate(a,b):
    sum=a+b
    difference=a-b
    multiplication=a*b
    division=a//b
    return sum,difference,multiplication,division
a=int(input('Enter Number: '))
b=int(input('Enter Number: '))
sum,difference,multiplication,division=calculate(a,b)
print(f"Sum:{sum},difference:{difference},multiply:{multiplication},Division:{division}")