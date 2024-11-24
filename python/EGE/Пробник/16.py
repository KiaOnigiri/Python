from sys import *
def F(n):
    if n==1:
        return 5
    if n>1:
        return 2*n+1+F(n-1)
setrecursionlimit(10000)
print(F(2024)-F(2022))
