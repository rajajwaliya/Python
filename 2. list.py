Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y="raj"
>>> len(y)
3
>>> x=123
>>> len(x)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    len(x)
TypeError: object of type 'int' has no len()
>>> nums=[20,30,40,50,60]
>>> len(nums)
5
>>> nums[3]
50
>>> num[2:]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num[2:]
NameError: name 'num' is not defined
>>> nums[2:]
[40, 50, 60]
>>> nums[-2]
50
>>> nums[-2:]
[50, 60]
>>> news=[30,"ajwaliya",'raj',3.8]
>>> news
[30, 'ajwaliya', 'raj', 3.8]
>>> listoflist=[news,nums]
>>> listoflist
[[30, 'ajwaliya', 'raj', 3.8], [20, 30, 40, 50, 60]]
>>> nums.append(90)
>>> nums
[20, 30, 40, 50, 60, 90]
>>> nums.insert(3,59)
>>> nums
[20, 30, 40, 59, 50, 60, 90]
>>> nums.remove(3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nums.remove(3)
ValueError: list.remove(x): x not in list
>>> nums.remove(59)
>>> nums
[20, 30, 40, 50, 60, 90]
>>> del nums[4:]
>>> nums
[20, 30, 40, 50]
>>> nums.extends([20,58,60])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    nums.extends([20,58,60])
AttributeError: 'list' object has no attribute 'extends'
>>> nums.extend([20,59,78])
>>> nums
[20, 30, 40, 50, 20, 59, 78]
>>> max(nums)
78
>>> min(nums)
20
>>> sum(nums)
297
>>> x=_
>>> x
297
>>> nums.short()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    nums.short()
AttributeError: 'list' object has no attribute 'short'
>>> nums.sort()
>>> nums
[20, 20, 30, 40, 50, 59, 78]
>>> 
