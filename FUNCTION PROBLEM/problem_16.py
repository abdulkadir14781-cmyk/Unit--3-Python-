def  total(sub1,sub2,sub3,sub4,sub5):
    return sub1+sub2+sub3+sub4+sub5
def avg(sum_):
    average=sum_/5
    return average
def display(sum_,average):
    print(f"Total={sum_}\nAverage={average}")

sub1=int(input('Enter Marks: '))
sub2=int(input('Enter Marks: '))
sub3=int(input('Enter Marks: '))
sub4=int(input('Enter Marks: '))
sub5=int(input('Enter Marks: '))
sum_=total(sub1,sub2,sub3,sub4,sub5)
average=avg(sum_)
display(sum_,average)