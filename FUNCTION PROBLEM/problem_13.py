def sum_of_digit(n):
    sum = 0
    while n>0:
        r=n%10
        sum+=r
        n=n//10
    return sum
n=int(input('Enter Number: '))
print(f"Sum of digit: {sum_of_digit(n)}")