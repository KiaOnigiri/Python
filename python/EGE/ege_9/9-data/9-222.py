def rep(x):
    return [z for z in x if x.count(z)>=2]
def unrep(x):
    return [z for z in x if x.count(z)==1]


f=open('9-222.txt')
s=f.read().splitlines()
s=[[int(z) for z in x.split('\t')] for x in s]
k=0
for x in s:
    k+=1
    if len(unrep(x))!=4:
        continue
    if rep(x)[0]>=(sum(unrep(x))/4):
        break
print(k)
