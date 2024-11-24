f=open('k7data\k7-m1.txt')
c=f.read()
k,kmin=0,len(c)+1
b=0
for i in range(len(c)):
    if c[i] == 'C':
        k+=1
    elif k!=0:
        b+=1
        kmin=min(kmin,k)
        k=0
        
if k!=0:
    kmin=min(kmin,k)
    b+=1
print(kmin,b,len(c))
