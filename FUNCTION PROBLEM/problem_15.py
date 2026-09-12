def get_grade(marks):
    if marks<=100 and marks >=90:
        grade="A"
    elif marks<=89 and  marks >=80:
        grade ="B"
    elif marks<=79 and marks >=70:
        grade ="C"
    elif marks<=69 and marks >=60:
        grade ="D"
    elif marks<60:
        grade="F"
        
    return grade
marks=int(input('Enter Marks: '))
print(f"Grade :{get_grade(marks)}")

    
