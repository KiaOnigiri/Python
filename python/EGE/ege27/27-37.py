f=open('C:/python/EGE/ege27/27-data/37/27-37a.txt')
s=f.read().splitlines()
s=s[1:]
s=[int(x) for x in s]
#print(s[:5])
b=[]
for i in range(len(s)):
    for j in range(1+i,len(s)):
        b.append([s[i]+s[j],j])
k=0
for x in b:
    k+=s[x[1]+1:].count(x[0])
print(k)
