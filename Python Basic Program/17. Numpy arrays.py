from numpy import *

arr = array([10,20,50],int)
print(arr)
print(arr.dtype)

linarry = linspace(0,10,7)
print("%.5f"%linarry[2])
print(linarry.dtype)


logarry = logspace(0,20,7)
print(logarry)
print(logarry.dtype)

arangearr = arange(0,20,7)
print(arangearr)
print(arangearr.dtype)

zeros= zeros(9)
print(zeros)
print(zeros.dtype)

one = ones(9,int64)
print(one)
print(one.dtype)