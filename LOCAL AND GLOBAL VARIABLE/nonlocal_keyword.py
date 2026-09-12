def Outer():
    x=10
    def inner():
        nonlocal x
        x=20
        print(f"Inner Function x:{x}")
    inner()
    print(f"Out of inner function x:{x}")
Outer()
