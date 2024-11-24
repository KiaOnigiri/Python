f=open("k7data/k7b-5.txt")
c=f.read()
k='CA'
while k in c:
    k+='CA'
k=k[:-2]
if k+'C' in c:
    k+='C'
print(len(k))
