x=10
def fun():
    global y
    y=20
    print(f"Inside Function y:{y}")
    print(f"Outside Function x:{x}")
fun()
print(f"Inside Function y:{y}")