from numpy import *

array1=array([[0,34,56],[89,87,7],[56,5,5]])

print(array1.ndim)
print(array1)

print(array1.shape)
print(array1.size)

arr2= array1.flatten()
print(arr2)

arr3=arr2.reshape(3,3)
print(arr3)

m1 =  matrix('1 4 3; 4 5 6; 7 8 7')
m2 = matrix('3 2 3; 6 6 6; 6 8 7')

print(m1)
print(m2)

m3=m1*m2

print(m3)