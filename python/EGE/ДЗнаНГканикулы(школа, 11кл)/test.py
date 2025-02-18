import itertools 
count = 0
s = itertools.product([0,1],repeat = 20)
for i in s:
    if (5 + sum(i))%5 !=0:
        count += 1
print(count)
