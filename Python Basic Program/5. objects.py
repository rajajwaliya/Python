Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> raj=200
>>> id(raj)
1897219440
>>> a=5
>>> b=5
>>> id(a)
1897216320
>>> id(b)
1897216320
>>> id(5)
1897216320
>>> a=7
>>> id(a)
1897216352
>>> id(b)
1897216320
>>> type(a)
<class 'int'>
>>> type(10)
<class 'int'>
>>> 
