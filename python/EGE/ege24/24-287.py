def onexy(s):
    k=0
    kx=0
    ky=0
    i=0
    b=[]
    while i<len(s):
        k+=1
        if s[i]=='X':
            kx+=1
            if kx>1 and ky==1:
                b.append(k-1)
                i=ix
                k=0
                kx,ky=0,0
            if kx>1:
                i=ix
                k=0
                kx,ky=0,0
            ix=i
        elif s[i]=='Y':
            ky+=1
            if ky>1 and kx==1:
                b.append(k-1)
                i=iy
                k=0
                kx,ky=0,0
            if ky>1:
                i=iy
                k=0
                kx,ky=0,0
            iy=i
        i+=1
    b.append(k)
    return max(b)

f=open('C:/python/EGE/ege24/24data/24-280.txt')
#s='ccXcccYccXccccYccYcccYXcccc'
s=f.read().split('A')
mx=0
for q in s:
    mx=max(mx,onexy(q))
print(mx)
