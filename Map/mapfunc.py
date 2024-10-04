"""map(function, iterable): Applies a given function to each item of an iterable (such as a list or tuple) and returns a map object.
Returns a map object which is an iterator, so we can iterate over its elements."""

def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


print(map(lambda x: x**2, [1, 2, 3, 4]))#returns a map object
print(list(map(lambda x: x**2, [1, 2, 3, 4])))





