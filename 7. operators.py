Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=2
>>> y=6
>>> x
2
>>> v
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> y
6
>>> x=x+2
>>> x
4
>>> x+=2
>>> x
6
>>> x=x*2
>>> x
12
>>> x*=3
>>> x
36
>>> x=12
>>> x=x*3
>>> x
36
>>> x=2
>>> x*5=4
SyntaxError: can't assign to operator
>>> x*=5
>>> x
10
>>> a,b=5,8
>>> a
5
>>> b
8
>>> a>b
False
>>> b>a
True
>>> a=6
>>> b=6
>>> a>=b
True
>>> a<=b
True
>>> a==b
True
>>> a==b and a<=b
True
>>> a!=b or a==b
True
>>> a=True
>>> a=not a
>>> a
False
>>> a==(not a)
False
>>> 
