f=open('D:/python/EGE/ege27/27-data/21/27-21b.txt')
s=f.read().splitlines()
s=s[1:]
s=[[int(y) for y in x.split()] for x in s]
k=0
b=[]
for x in s:
    k+=max(x)
    b.append(max(x)-min(x))
print(k,sorted(b)[800:1000])
#print(s[:5])
#13608
#40724928
