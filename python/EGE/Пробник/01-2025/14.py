s='0123456789'
for i in range(ord('A'),ord('A')+15):
    s+=chr(i)
print(s)
for x in s:
    if (int(f'11353{x}12',25)+int(f'135{x}21',25))%24==0:
        print(x,(int(f'11353{x}12',25)+int(f'135{x}21',25))/24)
