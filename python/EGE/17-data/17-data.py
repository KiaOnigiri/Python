f=open("17-1.txt")
s=f.read().splitlines()
s=[int(z) for z in s]
b=[]
for i in range(len(s)-1):
    if s[i]%7==0 and s[i+1]%17!=0 or s[i+1]%7==0 and s[i]%17!=0:
        b.append(s[i]+s[i+1])

print(len(b),min(b))
