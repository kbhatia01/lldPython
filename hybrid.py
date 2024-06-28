
class Parent:
    # def __init__(self, a):
    #     self.eye=3
    def __init__(self):
        self.eye = 2

    def display(self):
        # print(self.eye)
        print("display parent..")



class child(Parent):

    def __init__(self, age):
        self.eye = 1
        self.age=age

    def dummy(self):
        print("child method..")


class grand_child1(child):
    pass


class grand_child2(child):
    pass


parent1 = Parent()

parent1.dummy()