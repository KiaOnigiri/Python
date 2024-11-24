f=open("24-S1.txt")
s=f.read().splitlines()
g=0
r=0
for i in range(len(s)):
    if s[i].count('YZ')>1:
        g+=1
    
print(g)
