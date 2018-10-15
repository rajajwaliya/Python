from numpy import *

fun1= array([10,20,30,45])
fun2= array([3,23,30,43])

print(fun1+fun2)
print(sqrt(fun1))
print(min(fun2))

arry1 = array([10,50,48,55,56,70])
arry2 = arry1

print(arry1)
print(arry2)
print(id(arry1))
print(id(arry2))
arry1[3] = 57
print(arry1)
print(id(arry1))
print(id(arry2))

arry3 = array([13,33,55,56,70])
arry4 = arry3.view()

print(arry3)
print(arry4)
print(id(arry3))
print(id(arry4))
arry4[3] = 34
print(arry3)
print(id(arry3))
print(id(arry4))

arry4 = array([13,33,55,56,70])
arry5 = arry4.copy()

print(arry4)
print(arry5)
print(id(arry4))
print(id(arry5))
arry4[3] = 56
print(arry4)
print(id(arry4))
print(id(arry5))



