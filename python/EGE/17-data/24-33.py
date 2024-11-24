f=open('k7data\k7c-1.txt')
c=f.read()
print(c[:10])
k=0
for i in range(1,len(c)-1):
    if (c[i-1] in 'BCD') and (c[i] in 'BDE' and c[i]!=c[i-1]) and (c[i+1] in 'BCE' and c[i+1]!=c[i]):
        k+=1
print(k)
