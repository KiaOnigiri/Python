f=open('k7data\k7c-4.txt')
c=f.read()
k=0
for i in range(1,len(c)-1):
    if (c[i-1] in 'ADF' and c[i-1]!=c[i+1]) and (c[i] in 'CDF' and c[i]!=c[i+1]) and (c[i+1] in 'CDF'):
        k+=1
print(k)
