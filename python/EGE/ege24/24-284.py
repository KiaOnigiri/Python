def onexy(s):
    k=0
    kx=0
    ky=0
    kz=0
    i=0
    b=[]
    while i<len(s):
        k+=1
        if s[i]=='X':
            kx+=1
            if kx>3 and ky<=3 and kz<=3:
                b.append(k-1)
                i=ix
                k=0
                kx,ky,kz=0,0,0
            elif kx>3:
                i=ix
                k=0
                kx,ky,kz=0,0,0
            ix=i
        elif s[i]=='Y':
            ky+=1
            if ky>3 and kx<=3 and kz<=3:
                b.append(k-1)
                i=iy
                k=0
                kx,ky,kz=0,0,0
            elif ky>3:
                i=iy
                k=0
                kx,ky,kz=0,0,0
            iy=i
        elif s[i]=='Z':
            kz+=1
            if kz>3 and kx<=3 and ky<=3:
                b.append(k-1)
                i=iz
                k=0
                kx,ky,kz=0,0,0
            elif kz>3:
                i=iz
                k=0
                kx,ky,kz=0,0,0
            iz=i
        i+=1
    
    b.append(k)
    return max(b)

f=open('C:/python/EGE/ege24/24data/24-280.txt')
#s='ccXcccYccXccccYccYcccYXcccc'
s=f.read()
print(onexy(s))
#207
