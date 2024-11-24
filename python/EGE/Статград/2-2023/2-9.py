f=open('09.txt')
s=f.read().splitlines()
s=[x.split('\t') for x in s]
s=[[int(y) for y in x] for x in s]
k=0
for x in s:
    f=max(x)
    if len(set(x))!=len(x) and x.count(f)==1 and sum([g for g in x if x.count(g)>1])>f:
        k+=1
print(k)
