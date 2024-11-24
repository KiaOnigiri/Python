#print(len([1 for i in range(138,603885) if len(set(list(str(i))))!=len(list(str(i))) and i in [3**j for j in range(13)]]),min([z for z in range(138,603885) if len(set(list(str(z))))!=len(list(str(z))) and z in [3**j for j in range(13)] and sum([int(x) for x in list(str(z))])==max([sum([int(k) for k in list(str(3**j))]) for j in range(13) if len(set(list(str(3**j))))!=len(list(str(3**j)))])]))
from functools import *
mean = lambda x : sum(x) / len(x)
x = [5, 10, 15, 20]
print(mean(x))
current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
summa = reduce((lambda x, y: x * y), current_list)
print(list(summa))
tables = [lambda x=x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())
