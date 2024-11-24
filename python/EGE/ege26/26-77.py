f=open('26-77.txt')
s=f.read().splitlines()
n=s[0]
s=s[1:]
s=[[int(x) for x in z.split()]for z in s]
s=sorted(s)
b=[]
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        b.append(s[i])
b.append(s[i])
print(b)
k_all=0
k=1
kmax=0
year=0
for i in range(len(b)-1):
    if b[i][0]!=b[i+1][0]:
        if 8-k>=kmax:
            kmax=8-k
            year=b[i][0]
        k_all+=8-k
        print(f'year={b[i][0]} needed={8-k}')
        k=1
        continue
    k+=1
if 8-k>=kmax:
        kmax=8-k
        year=b[i][0]
k_all+=8-k
print(f'year={b[i][0]} needed={8-k}')
print(k_all,year)
