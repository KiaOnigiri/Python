f=open('26-s1.txt')
s=f.read().splitlines()
s=s[1:]
s=[int(z) for z in s]
s.sort()
cheap=0
for i in range(len(s)):
    if s[i]<=200:
        cheap+=s[i]
    else:
        break
s=s[i:]
fr=len(s)//2
sale=0
for i in range(fr):
    sale+=s[i]
sale=sale*0.7
rich=sum(s[fr:len(s)])
print(rich+sale+cheap,s[i])
