def min_max_dels(x):
    b=[]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            b.append(x//i)
            b.append(i)

    b=sorted(set(b))
    if b!=[]:
        return min(b)+max(b)
    else:
        return 0



x=800001
d=[]
while True:
    if str(min_max_dels(x))[-1]=='4':
        d.append(x)
    if len(d)==5:
        break
    x+=1

for m in d:
    print(f'{m}  {min_max_dels(m)}')
