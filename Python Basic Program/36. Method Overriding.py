class A:
    def show(self):
        print("method of A")

class B(A):
    def show(self):
        print("method of B")

obj=B()
obj.show()