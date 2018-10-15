from functools import *

ls=[10,55,33,20,66,77,88]

fil= list(filter(lambda a : a%2==0, ls))
print(fil)
ma = list(map( lambda a: a*2, fil))
print(ma)
red= reduce(lambda a,b: a+b,ma)
print(red)