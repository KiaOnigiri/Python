def mult(x):
    x=str(x)
    x=[int(z) for z in x]
    k=1
    for v in x:
        k*=v
    if k!=0:
        return k
    else:
        return 3558995


b=[]
for i in range(1111,9999+1):
    c=str(i)
    c=[int(z) for z in c]
    if i%mult(i)==0 and i%sum(c)==0:
        b.append(i)
o=0
for j in b:
    if j>o:
        o=j
print(len(b),o)
