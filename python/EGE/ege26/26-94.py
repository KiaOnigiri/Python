f=open('26-94.txt')
s=f.read().splitlines()
n,t=s[0].split()
n=int(n)
t=int(t)
s=s[1:]
s=[[int(x) for x in z.split()] for z in s]
s.sort()
s1=[]
s2=[]
for x in s:
    if x[0]==1:
        s1.append([x[1],x[2]])
    else:
        s2.append([x[1],x[2]])
sd1=dict()
sd2=dict()
for x in s1:
    if x[0] in sd1:
        sd1[x[0]].append(x[1])
    else:
        sd1[x[0]]=[x[1]]
for x in s2:
    if x[0] in sd2:
        sd2[x[0]].append(x[1])
    else:
        sd2[x[0]]=[x[1]]
ans1=0
ans11=0
ans2=0
for k,v in sd1.items():
    if (1 not in v and 2 not in v and 3 not in v and 4 not in v) or (t not in v and t-1 not in v and t-2 not in v and t-3 not in v):
        ans1=k
        ans2+=1
for k,v in sd2.items():
    if (1 not in v and 2 not in v and 3 not in v and 4 not in v) or (t not in v and t-1 not in v and t-2 not in v and t-3 not in v):
        ans11=k
        ans2+=1
print(max(ans11,ans1),ans2)
        
