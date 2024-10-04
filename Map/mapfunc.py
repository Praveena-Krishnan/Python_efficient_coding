"""map(function, iterable): Applies a given function to each item of an iterable (such as a list or tuple) and returns a map object.
Returns a map object which is an iterator, so we can iterate over its elements."""

print(map(lambda x: x**2, [1, 2, 3, 4]))#returns a map object
print(list(map(lambda x: x**2, [1, 2, 3, 4])))



