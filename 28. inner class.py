class Mainclass:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.city = self.City()


    def show(self):
        print("the id {} and name {}".format(self.id,self.name))
        self.city.show()


    class City:
        def __init__(self):
            self.city='bhavnagar'


        def show(self):
            print("the city {}".format(self.city))


myobj=Mainclass(5,'raj')
myobj.show()
