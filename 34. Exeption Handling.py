
a=10
b=2

try:
    print("hello")
    c=a/b
    print(c)
    d=int(input("enter int number :- "))
    print(d)
except ZeroDivisionError as e:
    print("Divide BY Zero error",e)
except ValueError as e:
    print("Invalid Input",e)
except Exception as e:
    print(e)

finally:
    print("Bye")


