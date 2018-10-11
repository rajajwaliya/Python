from array import *
import numpy

arr=array('i',[10,20,40,-29,89])
newarr=array(arr.typecode,(a*3 for a in arr))

arr.reverse()
newarr.reverse()


print(arr)
print(newarr)
print(newarr.buffer_info())
print(arr.buffer_info())

mydemoarr=array('i',[])

n= int(input("Enter lenth of array :- "))
i=0
for i in range(n):
    x = int(input("Enter value in array :- "))
    mydemoarr.append(x)

f= int(input("enter value that your find :- "))
i=0
k=0
for i in mydemoarr:
    if f==i:
        print(k+1)
        break

    k+=1
