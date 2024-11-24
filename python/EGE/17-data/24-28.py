f=open("k7data/k7b-2.txt")
c=f.read()
k='DBAC'
while k in c:
    k+='DBAC'
k=k[:-4]
if k+'DBA' in c:
    k+='DBA'
elif k+'DB' in c:
    k+='DB'
elif k+'D' in c:
    k+='D'
print(len(k))
