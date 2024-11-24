def sp_predkov(p1):
    if rod.get(p1)==None:
        return [p1]
    parent=rod[p1]
    if rod.get(parent)!=None:
        return [parent]+sp_predkov(parent)
    else:
        return [parent]
def LCA(sp1,sp2):
    b=[]
    for i in range(len(sp1)):
        if sp1[i]==sp2[i]:
            b.append(sp1[i])
        else:
            return b[-1]
    return b[-1]
    
            

f=open('derevo.txt')
s=f.read().splitlines()
rod={}
for line in s:
    child,parent=line.split()
    rod[child]=parent
p1='K'
sp1=sp_predkov(p1)[::-1]
p2='J'
sp2=sp_predkov(p2)[::-1]
print(sp1,sp2,LCA(sp1,sp2))
