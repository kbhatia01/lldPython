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


