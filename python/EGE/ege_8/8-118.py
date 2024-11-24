from itertools import permutations
k=0
for x in set(permutations('АВРОРА')):
    x=''.join(x)
    if 'АА' in x or 'РР' in x:
        continue
    k+=1
print(k)
