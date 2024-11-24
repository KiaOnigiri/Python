f=open('24-157.txt')
s=f.read()
c=[0]*26
for i in range(2,len(s)):
    if s[i-2]==s[i-1]:
        c[ord(s[i])-ord('A')]+=1
print(chr(c.index(max(c))+ord('A')),max(c),sep='')
