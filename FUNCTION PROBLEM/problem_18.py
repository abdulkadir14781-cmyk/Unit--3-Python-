def display(bill):
    print(f"Electricity Bill: {bill}")

def calculate_bill(unit,rate):
    bill=unit*rate
    display(bill)
    
def get_unit():
    unit=int(input('Enter Unit: '))
    rate=int(input('Enter rate: '))
    calculate_bill(unit,rate)
get_unit()
