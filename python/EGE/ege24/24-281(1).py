f=open('C:/python/EGE/ege24/24data/24-280.txt')
s=f.read()
b=[0,0,0]
mx=0
for x in range(len(s)):
    k=0
    for y in range(x-1,len(s)):
        if s[y]=='X':
            b[0]+=1
        if s[y]=='Y':
            b[1]+=1
        if s[y]=='Z':
            b[2]+=1
        k+=1
        if any([p>5 for p in b]):
            mx=max(mx,k-1)
            b=[0,0,0]
            k=0
            break
    mx=max(mx,k-1)
    b=[0,0,0]
    k=0
print(mx)
