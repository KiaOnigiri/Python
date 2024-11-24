f=open('k7data\k7-m22.txt')
#s='FDCBA'
s=f.read()
b=[]
for i in range(1,len(s)-1):
    c=[s[i-1],s[i],s[i+1]]
    if sorted(c, reverse=True)==c and len(set(c))==3:
        b.append(c)
        ip=i-1
print(len(b),ip)
