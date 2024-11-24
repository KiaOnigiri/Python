f=open('26-101.txt')
s=f.read().splitlines()
n,k=s[0].split()
k=int(k)
s=s[1:]
s=[int(z) for z in s]
s.sort(reverse=True)
#print(s[:5])
cnt=0
g=0
while s:
    idx=[0]
    box=[s[0]]
    for i in range(1,len(s)):
        if box[-1]-s[i]>=k:
            box.append(s[i])
            idx.append(i)
    s=[s[i] for i in range(len(s)) if i not in idx]
    cnt+=1
    if g==0:
        g=len(box)
print(cnt,g)
