f=open('17ПК1.txt')
s=f.read().splitlines()
s=[int(y) for y in s]
b=[]
for i in range(1,len(s)):
    if 100<=(abs(s[i-1])+abs(s[i]))<=700:
        b.append(s[i-1])
        b.append(s[i])
print(len(b)/2,max(b))
#11 387
