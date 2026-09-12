
x="global"
def Outer():
    x="Outer local"
    def inner():
        x="inner local"
        print(f"Inner Function x:{x}")
    inner()
    print(f"Outer function x:{x}")
Outer()
print(f"Outside outer function x:{x}")
