import statistics
f=open('24-179.txt')
s=f.read()
b=[]
h=0
for i in range(4,len(s)):
    if s[i-4]=='C' and s[i-3]=='B' and (s[i-2]=='C' or s[i-2]=='D' or s[i-2]=='E') and s[i-1]=='B' and s[i]=='C':
        b.append(s[i-2])
        h+=1
print(statistics.mode(b),h)
