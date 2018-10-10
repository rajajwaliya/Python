Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> type(a)
<class 'int'>
>>> b=5.0
>>> type(b)
<class 'float'>
>>> c=5+7j
>>> type(c)
<class 'complex'>
>>> d=b>c
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d=b>c
TypeError: '>' not supported between instances of 'float' and 'complex'
>>> bool=b>a
>>> bool
False
>>> a=float(b)
>>> type(a)
<class 'float'>
>>> b=int(b)
>>> type(b)
<class 'int'>
>>> a=complex(b+aj)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a=complex(b+aj)
NameError: name 'aj' is not defined
>>> a=complex(b+a)
>>> type(a)
<class 'complex'>
>>> a=int(bool)
>>> bool=false
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    bool=false
NameError: name 'false' is not defined
>>> a
0
>>> b
5
>>> c
(5+7j)
>>> bool=a>b
>>> int(bool)
0
>>> bool=a<b
>>> int(bool)
1
>>> l=[10,20,30,40,50]
>>> l
[10, 20, 30, 40, 50]
>>> type(l)
<class 'list'>
>>> t=(10,20,30,40)
>>> t
(10, 20, 30, 40)
>>> type(t)
<class 'tuple'>
>>> range(10)
range(0, 10)
>>> type(range(10))
<class 'range'>
>>> s={10,20,30,40}
>>> s
{40, 10, 20, 30}
>>> tpye(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    tpye(s)
NameError: name 'tpye' is not defined
>>> type(s)
<class 'set'>
>>> l=[range(0,10)]
>>> l
[range(0, 10)]
>>> l=list(range(0,10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,9,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> list(range(0,9,2))
[0, 2, 4, 6, 8]
>>> d={'name':'raj','city':'bhavnagar','word':'developer'}
>>> type(d)
<class 'dict'>
>>> d.get('name')
'raj'
>>> d['city']
'bhavnagar'
>>> d.keys
<built-in method keys of dict object at 0x00397B70>
>>> d.keys()
dict_keys(['name', 'city', 'word'])
>>> d.values()
dict_values(['raj', 'bhavnagar', 'developer'])
>>> 
