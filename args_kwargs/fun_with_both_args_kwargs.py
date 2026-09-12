def fun(*a,**kwargs):
    print(a,type(a))
    print(kwargs,type(kwargs))
fun(1,2,3,4,name="Abdul",age=17)