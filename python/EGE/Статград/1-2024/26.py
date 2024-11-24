f=open('26.txt')
s=f.read().splitlines()
colvoclientov=s[0]
s=s[1:]
s=[[int(y) for y in x.split()]+[0] for x in s]
s=sorted(s)
#print(s[:5])
minchel=0#min vremyaprihoda
maxchel=899+40+15#max vremyaprihoda + ozhidanie + max vremyaobsl
zanyato=[0,0,0,0,0,0]
colvoobsl=[0,0,0,0,0,0]
for time in range(minchel,maxchel+1):
    for p in range(len(s)):
        if (time-40<=s[p][0]<=time) and zanyato[s[p][2]-1]==0 and s[p][3]==0:
            zanyato[s[p][2]-1]=s[p][1]
            colvoobsl[s[p][2]-1]+=1
            s[p][3]=1
    for m in range(len(zanyato)):
        if zanyato[m]!=0:
            zanyato[m]-=1
print(max(colvoobsl))
k=0
for i in range(len(s)):
    if s[i][3]==0:
        k+=1
print(k)
