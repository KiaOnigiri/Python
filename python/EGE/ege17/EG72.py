b=[]
for i in range(2848,109499+1):
    i=str(i)
    i=[int(j) for j in i]
    k=[]
    for g in range(len(i)):
        if i[g]>5:
            k.append(i[g])
    if 9 in i and sum(k)%3==0:
        b.append(''.join([str(z) for z in i]))
a=0
for v in b:
    v=int(v)
    f=str(v)
    f=[int(j) for j in f]
    if v//(10**(len(f)-1))==8 and a<v:
        a=v
print(len(b),a)
