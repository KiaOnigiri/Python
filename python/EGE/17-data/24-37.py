f=open("k7data/k7c-5.txt")
c=f.read()
k,kmax=0,0
for i in range(4,len(c)):
    if c[i-4]!=c[i-3] and c[i-3]!=c[i-2] and c[i-2]!=c[i-1] and c[i-1]!=c[i]:
        k+=1
print(k)
