class Std:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result1=self.x+other.x
        result2=self.y+other.y
        stdobj=Std(result1,result2)
        return stdobj

    def __str__(self):
        return "{} {}".format(self.x,self.y)

obj = Std(12, 23)
obj2 = Std(34,89)
obj3=obj+obj2
print(obj3.x)
print(obj3.y)
print(obj3)