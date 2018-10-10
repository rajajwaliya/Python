Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=[10,20,30,40]
>>> l
[10, 20, 30, 40]
>>> t=(22,33,44,55)
>>> t
(22, 33, 44, 55)
>>> t.count
<built-in method count of tuple object at 0x03444210>
>>> t.index[5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t.index[5]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> t.index(2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t.index(2)
ValueError: tuple.index(x): x not in tuple
>>> t.index
<built-in method index of tuple object at 0x03444210>
>>> s={30,40,50,60,50,30}
>>> s
{40, 50, 60, 30}
>>> s.difference
<built-in method difference of set object at 0x0345FF30>
>>> s.remove(50)
>>> s
{40, 60, 30}
>>> 
