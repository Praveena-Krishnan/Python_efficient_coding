"""_summary_Write a Python for loop in one line to iterate over a list of numbers from 1 to 10 and print each number.
"""
print([x for x in range(1,11) if x%2==0])#even numbers


result = [(i, j) for i in range(1, 4) for j in range(1, 3)]
print(result)