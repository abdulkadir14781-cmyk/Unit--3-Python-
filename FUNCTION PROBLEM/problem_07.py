def student_result(marks):
    sum_marks=sum(marks)
    avg=sum_marks/len(marks)
    Highest=max(marks)
    Lowest=min(marks)
    return sum_marks,avg,Highest,Lowest
marks=[1,2,3,4,3]
sum_,avg,Highest,Lowest=student_result(marks)
print(f"sum:{sum_} Higest marks:{Highest} Lowest maeks:{Lowest} average:{avg}")