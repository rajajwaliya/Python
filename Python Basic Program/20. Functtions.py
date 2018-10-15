def dem0():
    print("this is basic function")
    print("demo function")

def addandsub(x,y):
    return (x+y),(x-y)

dem0()
num1,num2 = addandsub(5,8)
print(num1,num2)

def sum(*v):
    c=0
    for i in v:
        c=i+c
    print(c)

sum(4,6,7,-8,8)


#keyword veriable lenth argument

def sum2(n,**v1):
    print(n)
    for i,j in v1.items():
        print(i,j)


sum2(4,id="007",name="raj")

a=10
b=20
print(id(a))


def locglo():
    global a
    a=5
    b=50
    print(id(a))
    print(b)
    print(globals(b))

print(a)
print(id(a))
print(b)
print(id(b))