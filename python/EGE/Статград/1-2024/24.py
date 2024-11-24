#f=open('24.txt')
#s=f.read()
s='AAAXAAYAAXAAAYAXAAAAY'
b='UVWXYZ'
ind=[i for i in range(len(s)) if s[i] in b]
ind2=[s[i] for i in range(len(s)) if s[i] in b]
c=[0,0,0,0,0,0]
k=0
mx=0
c1=[0,0,0,0,0,0]
for i in range(len(ind)):
    k=i
    if ind2[i]=='U':
        c[0]+=1
        if c1[0]==0:
            c1[0]+=i
    if ind2[i]=='V':
        c[1]+=1
    if ind2[i]=='W':
        c[2]+=1
    if ind2[i]=='X':
        c[3]+=1
    if ind2[i]=='Y':
        c[4]+=1
    if ind2[i]=='Z':
        c[5]+=1
    if any([j>2 for j in c]):
        mx=max(mx,k)
        
