def fact(x):

    result=1
    for i in range(1,x+1):
        result=result*i
    return result

y=int(input("enter value you want to factorial :- "))
x=fact(y)
print(x)