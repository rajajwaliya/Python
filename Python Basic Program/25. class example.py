class Myclass:
    city="bhvn"

    def __init__(self, name):
        self.name = name

    def demo(self):
        print("hello welcome ", self.name)

    def compare(self,other):
        if(self.name==other.name):
            print("same name")
        else:
            print("diffrent name")

    @classmethod
    def citymethod(cls):
        print("your city is",cls.city)

    @staticmethod
    def byemethod():
        print("good bye")


obj = Myclass('raj')
obj2= Myclass('me')
Myclass.demo(obj)
obj.demo()
obj.compare(obj2)
Myclass.citymethod()
Myclass.byemethod()