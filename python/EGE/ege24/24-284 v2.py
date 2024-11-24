f=open('C:/python/EGE/ege24/24data/24-280.txt')
s=f.read()
#s='ccXcccYccXccccYccYcccYXcccZcccccccccc'
lim=3
cnt={'X':0,'Y':0,'Z':0}
mx=0
k=0
for L in range(len(s)):
    for R in range(L,len(s)):
        k+=1
        if s[R] in 'XYZ':
            cnt[s[R]]+=1
        if any([v>lim for k,v in cnt.items()]):
            mx=max(mx,k-1)
            k=0
            break
    cnt={'X':0,'Y':0,'Z':0}
    mx=max(mx,k)
    k=0
print(mx)
