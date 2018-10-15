class Student:
    def sum(self,x=None,y=None,z=None):
        sum=0

        if(x!=None and y!=None and z!=None):
            sum = sum + x + y + z
            return sum
        elif (x!= None and y!=None):
            sum = sum + x + y
            return sum
        elif(x!=None):
            sum=sum+x
            return sum
        else:
            return sum


std=Student()
print(std.sum(4,5))
print(std.sum())
print(std.sum(67,78,89))
print(std.sum(4))