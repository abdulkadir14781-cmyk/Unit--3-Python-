def check_result(avg):
    if avg>=40:
        return "Pass"
    else:
        return "Fail"
    
def display(result):
    print(f"Name:{name}\nTotal:{Total}\nAverage:{avg}\nResult:{result}")
               
def average(Total):
    global avg 
    avg= Total/5
    result=check_result(avg)
    display(result)

def total(marks):
    global Total
    Total=sum(marks)
    average(Total)

def input_():
    global name
    name=input('Enter Name: ')
    marks=[]
    for i in range(5):
        marks.append(int(input('Enter Number: ')))
    total(marks)
input_()