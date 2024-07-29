from functools import reduce
mul = lambda x,y : x*y

print(mul(2,3))

is_even = lambda x: x % 2 == 0

print(is_even(2))

# MAP, filter, Reduce

nums = [1,2,3,4,5]

square = list(map(lambda x: x**2, nums))
print(square)

even_filter = list(filter(lambda x: x%2==0, nums))

print(even_filter)

nums= [1,2,3,4,5]


total = reduce(lambda x,y: x+y, nums)

print(total)


max_value = reduce(lambda x,y : max(x,y), nums)

print(max_value)

print(max(nums))










words = ["hello", " ", "world"]

conc = reduce(lambda x,y : x+y, list(filter(lambda word: word!=" ", words)))

print(conc)



