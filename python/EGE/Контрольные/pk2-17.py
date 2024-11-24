f=open('17ПК2.txt')
s=f.read().splitlines()
s=[int(x) for x in s]
b=[]
for i in range(len(s)-1):
    if (s[i]+s[i+1])>=50 and (s[i]>=0) and (s[i+1]>=0):
        b.append(s[i]*s[i+1])
print(len(b),min(b))
