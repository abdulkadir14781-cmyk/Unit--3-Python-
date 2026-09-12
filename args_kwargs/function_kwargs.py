def fun(**a):    #return dictionary
    print(a)
    print(type(a))
    for key in a:
        print(key)
    for value in a.values():
        print(value)
    for key,value in a.items():
        print(f"{key}:{value}")
fun(name="Abdul",section="2A",age=17)