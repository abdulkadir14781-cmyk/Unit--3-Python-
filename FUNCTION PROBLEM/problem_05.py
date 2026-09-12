import math
def area_circle(radias):
    return math.pi*radias*radias
radias=float(input('Enter radias of circle: '))
print(f"Area of circle:{round(area_circle(radias),2)}")