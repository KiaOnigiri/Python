f=open('k7data\k7-m25.txt')
#s='FDCBA'
s=f.read()
b=[]
for i in range(1,len(s)-1):
    c=[s[i-1],s[i],s[i+1]]
    if s[i-1]<s[i]>s[i+1]:
        b.append(c)
        ip=i-1
print(b)
print(len(b),ip)
