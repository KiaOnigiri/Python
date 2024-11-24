f=open('26-42.txt')
s=f.read().splitlines()
sp,fund=[int(x) for x in s[0].split()]
s=s[1:]
s2=[]
for x in s:
    x=x.split()
    s2.append([x[0],int(x[1]),int(x[2])])
s2.sort(key=lambda x: [-ord(x[0]),x[1]])
sumZ=sum([x[1]*x[2] for x in s2 if x[0]=='Z'])
fund=fund-sumZ
sumA=0
count=0
for i in range(len(s2)):
    if s2[i][0]=='A':
        if sumA+(s2[i][1]*s2[i][2])>fund:
            break
        sumA+=s2[i][1]*s2[i][2]
        count+=s2[i][2]
print(sumA)
f=0
k=0
for j in range(s2[i][2]):
        if f+s2[i][1]>(fund-sumA):
            break
        f+=s2[i][1]
        k+=1
print(k+count, fund-sumA-f)
