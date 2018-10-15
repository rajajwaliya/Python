class Myname:
    def execute(self):
        print("my name method")


class Othername:
    def execute(self):
        print("my name method other")
        print("second method")

class Mymain:
    def main(self,duc):
        duc.execute()

name=Myname()
other=Othername()

obj=Mymain()
obj.main(other)
