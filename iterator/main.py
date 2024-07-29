my_list = ["today", "7days..", "week"]

data = []
for i in my_list:
    data.append(i)

# return data

iterator = iter(my_list)

print(next(iterator)) # 1
# complex operation and it takes 5 sec...
# return today
print(next(iterator))
# return 7 days graph

print(next(iterator))
# return month graph...



class my_iterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            temp = self.start
            self.start+=1
            return temp
        else:
            raise StopIteration

    def __reset__(self):
        self.start = 1

ite = my_iterator(1, 5)

print(next(ite))

ite.__reset__()

for i in ite:
    print(i)


#  GENERATORS...

def my_generator():
        yield




#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

print("fib.....")
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib_generator()

for _ in range(10):
    print(next(gen))

for _ in range(10):
    print(next(gen))