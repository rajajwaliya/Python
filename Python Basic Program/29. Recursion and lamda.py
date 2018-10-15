import sys

sys.getrecursionlimit()

def fact(n):
        if(n==0):
            return 1
        return n*fact(n-1)

x=fact(6)
print(x)

fun=lambda a : a+a

n=fun(6)
print(n)