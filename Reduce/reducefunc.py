"""Apply a function of two arguments cumulatively to the elements of a list, from left to right, so as to reduce the list to a single output.
The function reduces the list by applying a binary function (function of two arguments) to all items in the list, going from left to right, so as to reduce the list to a single output."""
    

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

