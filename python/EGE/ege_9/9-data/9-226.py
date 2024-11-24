def rep(x):
    return [z for z in x if x.count(z)==2]
def unrep(x):
    return [z for z in x if x.count(z)==1]


f=open('9-226.txt')
s=f.read().splitlines()
s=[[int(z) for z in x.split('\t')] for x in s]
k=[]
#print(rep([1,1,2,3,4,5]))
for x in s:
    if len(rep(x))!=4 and len(unrep(x))!=3:
        continue
    if max(unrep(x))==max(x):
        k=x
        break
print(sum(k),k)
