def count_number(number):
    count_positive = 0
    count_negative = 0
    count_zero = 0
    for i in number:
        if i>0:
            count_positive+=1
        elif i<0:
            count_negative+=1
        elif i==0:
            count_zero+=1
    return count_zero,count_negative,count_positive
number = [1,2,3,0,-40,0,-4,0]
zero,negative,positive = count_number(number)
print(f"No. of zero:{zero}")
print(f"No. of Negative Number:{negative}")
print(f"No. of Positive Number:{positive}")
