f=open("k7data/k7b-3.txt")
c=f.read()
k='BAFE'
while k in c:
    k+='BAFE'
k=k[:-4]
print(k)
if k+'BAF' in c:
    k+='BAF'
elif k+'BA' in c:
    k+='BA'
elif k+'B' in c:
    k+='B'
print(len(k))
