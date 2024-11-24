from itertools import *
for rep in range(0,3+1):
  print(f'repeat={rep}')
  for g in product(range(0,9+1),repeat=rep):
    g=''.join([str(x) for x in g])
    for p in '0123456789':
        x=f'1{g}4022{p}9'
        if int(x)%1987==0:
            print(x)
