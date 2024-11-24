f=open('24-181.txt')
s=f.read()
s=s.split('.')
k=0
kmax=0
for i in range(len(s)):
    if s[i].count('A')+s[i].count('E')+s[i].count('I')+s[i].count('O')+s[i].count('U')+s[i].count('Y')<=7:
        k=len(s[i])
        kmax=max(k,kmax)
print(kmax)
print(len(max(s,key=len)))
