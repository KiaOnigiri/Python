f=open('26-79.txt')
s=f.read().splitlines()
n,k=[int(z) for z in s[0].split()]
s=s[1:]
print(s[:5])
s=[[int(x) for x in z.split()] for z in s]
print(s[-5:])
s.sort()

row=0
place=0
for i in range(1,len(s)):
    if s[i-1][0]==s[i][0]:
        if s[i][1]-s[i-1][1]==k+1:
            row=s[i][0]
            place=s[i-1][1]+1
print(row,place)
