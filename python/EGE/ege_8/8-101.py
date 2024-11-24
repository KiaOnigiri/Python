from itertools import permutations
k=0
for x in set(permutations('ШАНЕЛЬ')):
    x=''.join(x)
    if x[0]!='Ь' and 'ЕАЬ' not in x:
        k+=1
print(k)
