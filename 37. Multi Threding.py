from threading import *
from time import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.5)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.5)


obj1 = Hello()
obj2 = Hi()
# obj1.run()
# obj2.run()
obj1.start()
sleep(0.2)
obj2.start()
obj1.join()
obj2.join()
print("Bye")
