f=open('26-59.txt')
s=f.read().splitlines()
n=int(s[0])
s=s[1:]
s=[[int(x) for x in z.split()] for z in s]
s.sort(key= lambda x: [-x[0],x[1]])
for i in range(1,len(s)):
    if s[i-1][0]==s[i][0] and s[i][1]-s[i-1][1]==3:
        break
print(s[i-1][0],s[i-1][1]+1)
