#name1, name2 = input("Enter two names separated by space: ").split()
n1="arun"
n2="sana"

common_letters=set(n1).intersection(set(n2))

n1_updated=[x for x in n1 if x not in common_letters]
n2_updated=[x for x in n2 if x not in common_letters]

print(n1_updated,n2_updated)
