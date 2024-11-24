def progressia(x):
    s=0
    for i in range(1,x):
        s+=i
    return s


a=[int(x) for x in open('C:/python/EGE/ege27/27-data/37/27-37b.txt')][1:]
rep=[0]*(max(a)+1)
k=0
for x in a:
    for y in range(1,x//2+x%2):
        k+=rep[y]*rep[x-y]
    if x%2==0:
        k+=progressia(rep[x//2])
    rep[x]+=1
print(k)
            
