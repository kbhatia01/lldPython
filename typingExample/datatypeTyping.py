from typing import List, Optional, Any

# age: int = 10
#
# print(age)
# age = 10
#
# print(age)


#  Typing techniques..

sqr: float = 0


def squareDiveideBy2(num: float) -> float:
    print(num * num)
    return num * num // 2


sqr = squareDiveideBy2(10.00)


def square(num: float) -> None:
    print(num * num)


square(10.00)

# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "abc"]
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)

numbDict: dict[int, str] = {1: "abc", 2: "def", 3: "ghi"}
# numbDict: dict[int, str] = {1:"abc", 2:"def","ghi": 3}

print(numbDict)

# numbSet: set[str] = {"abc","def","ghi", 2}
numbSet: set[str] = {"abc", "def", "ghi"}

print(numbSet)

# ll: list[list[int]]  = [[1,"asn",5], [2,4,5]]
ll: list[list[int]] = [[1, 2, 5], [2, 4, 5]]

vector = list[list[int]]

ll2: vector = [[1, 2, 5], [2, 4, 5]]

print(ll2)


def greet(name: Optional[str] = None) -> str:
    return f"Hello {name}"


print(greet())


def printingMethod(val: Any):
    print(val)


printingMethod(["1"])


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def getPersonName(person: Person) -> str:
    return person.name


getPersonName(Person("John", 20))

# GENERICS..

from typing import Generic, TypeVar, Type

M = TypeVar('M')


class Stack(Generic[M]):
    def __init__(self) -> None:
        self.stack: list[M] = []

    def push(self, item: M) -> None:
        self.stack.append(item)

    def pop(self) -> M:
        return self.stack.pop()


stack1 = Stack[int]()

# class StackInt():
#     def __init__(self) -> None:
#         self.stack: list[int] = []
#
#     def push(self, item: int) -> None:
#         self.stack.append(item)
#
#     def pop(self) -> int:
#         return self.stack.pop()


T = TypeVar('T', int, float)


def add(a1: T, a2: T) -> T:
    return a1 + a2


add(1.0, 1.0)


class A:
    def __init__(self, x: int) -> None:
        self.x = x

class B(A):
    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)

class C(A):
    def __init__(self, x: int) -> None:
        self.x = x
        super().__init__(x)

G = TypeVar('G', bound=A)

