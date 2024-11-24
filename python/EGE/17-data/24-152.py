f=open('24-j9.txt')
s=f.read()
g=0
for i in range(len(s)//2):
    if s[i]==s[-i-1]:
        g+=1
print(g)
