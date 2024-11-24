from random import *
n=10
b=[randint(1,99) for i in range(n)]
print(b)
k=int(input())
b=b[-k:]+b[:-k]
print(b)
