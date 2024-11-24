f=open('26-103.txt')
s=f.read().splitlines()
n,k,m=s[0].split()
n=int(n)
k=int(k)
m=int(m)
s=s[1:]
s=[[x for x in z.split()] for z in s]
s=[[int(one),two] for one,two in s]
s.sort(reverse=True)
print(s[:5])
cnt=0
maxcnt=0
while s:
    idx=[0]
    box=[s[0]]
    for i in range(1,len(s)):
        if box[-1][0]-s[i][0]>=k and box[-1][1]!=s[i][1]:
            box.append(s[i])
            idx.append(i)
            if len(idx)==m:
                maxcnt+=1
                break
    s=[s[i] for i in range(len(s)) if i not in idx]
    print(box)
    cnt+=1
print(cnt,maxcnt)
