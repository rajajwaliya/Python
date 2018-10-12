class A:
    def __init__(self):
        print("init method of a")

    def method1(self):
        print("class a method 1")

    def method2(self):
        print("class a method 2")


class B:
    def __init__(self):
        print("init method of b")


    def method3(self):
        print("class b method")

class C(A,B):
    def __init__(self):
        print("init method of c")
        super().__init__()


    def method4(self):
        print("clas c method")


c= C()
c.method1()
c.method2()
c.method3()
c.method4()
