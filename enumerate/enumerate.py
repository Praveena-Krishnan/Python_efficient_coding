"""
enumerate(iterable, start=0): Returns an enumerate object that produces tuples containing a count (from start, which defaults to 0) and the values obtained from iterating over the sequence.
The enumerate function is commonly used to loop over a list and have an automatic counter/index along with the values.

"""
l1=["mango","python","dog"]
print(list(enumerate(l1,100)))#returns the list with count starting from 100

l2=enumerate(l1)
print(next(l2)) #like iteration, it prints the next next element. 
print(next(l2))
#reversed list enumerate function
print(list(enumerate(reversed(l1))))#prints only the reverse of the 

for index , value in enumerate(reversed(l1)):
    print(len(l1)-index-1,value)#prints in reverse order of both index and value

    
    
    