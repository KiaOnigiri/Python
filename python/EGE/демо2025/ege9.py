f=open('ege9.txt')
s=f.read().splitlines()
s=[[int(y) for y in x.split()]for x in s]
k=0
for line in s:
    k3=[y for y in line if line.count(y)==3]
    k1=[y for y in line if line.count(y)==1]
    if len(k3)==3 and len(k1)==3:
        if sum(k3)**2>sum(k1)**2:
            k+=1
print(k)
