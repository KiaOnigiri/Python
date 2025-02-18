f=open('24_314.txt')
s=f.read()
s1=s.split('T')
b=[]
for i in range(len(s1)-1):
    if s1[i].count('O')==0 and s1[i+1].count('O')==0:
        b.append(len(s1[i])+len(s1[i+1])+1)
s2=s.split('O')
b1=[]
for x in s2:
    if x.count('T')<=1:
        b1.append(len(x))
print(max(max(b),max(b1)))
