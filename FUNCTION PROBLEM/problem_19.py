def generate_bill(total):
    print(f"Total Bill: {total}")
    
def calculate_Discount(total):
    discount=total*.20
    total=total-discount
    generate_bill(total)

def calculate_total(item_price,quantity):
    total=item_price*quantity
    calculate_Discount(total)

def input_items():
    item_price=float(input('Enter Item Price: '))
    quantity=int(input('Enter quantity: '))
    calculate_total(item_price,quantity)
input_items()
    