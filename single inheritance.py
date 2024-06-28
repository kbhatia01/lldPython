
class Parent:
    def __init__(self, a):
        self.eye=3
    def __init__(self):
        self.eye = 2

    def display(self):
        # print(self.eye)
        print("display parent..")



class child(Parent):

    def __init__(self, age):
        self.eye = 1
        self.age=age
        # super().display()


c = child(10)
c.display()