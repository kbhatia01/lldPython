class Base:
    def __init__(self):
        print("Base class constructor")
        self.base_attr = "Base attribute"

    def base_method(self):
        print("Base method")

class parent1(Base):
    def __init__(self):
        print("parent 1 const..")
        self.nose = 1
    def func(self):
        print("parent 1..")

    def func1(self):
        print("func 1..")

class parent2(Base):
    def __init__(self):
        print("parent 2 const..")

        self.name = "abc"
    def func(self):
        print("parent 2..")


class child(parent1, parent2):
    def __init__(self):
        # parent1.__init__(self)
        parent2.__init__(self)


c = child()

parent2.func(c)

print(c.func1())


print(child.mro())