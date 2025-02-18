f=open('24_314.txt')
s=f.read()
s=s.split('O')
b=[]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        b.append(len(s[i])*2+3)
print(max(b))
