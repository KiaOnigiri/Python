f=open('C:/python/EGE/ege24/24data/24-280.txt')
s=f.read()
s='ccccZcccXcccXcccYccccXcccccccZccccYccccccZcccZXcccccYccc'
lim=2
lx=[i for i,q in enumerate(s) if q=='X']
ly=[i for i,q in enumerate(s) if q=='Y']
lz=[i for i,q in enumerate(s) if q=='Z']
print(lx)
print(ly)
print(lz)
cnt={'X':lx,'Y':ly,'Z':lz}
L=0
