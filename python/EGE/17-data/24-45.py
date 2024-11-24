f=open('k7data\k7-m7.txt')
s=f.read()
#print(s[:10])
k=0
b=[]
for z in s:
    if z=='C':
        k+=1
    elif k>0:
        b.append(k)
        k=0
if k>0:
    b.append(k)
p=1
for z in b:
    p*=z
print(len(b))
print(s[:35])
print(sum(b),'C'*24,p,'AAABB',sep='')
