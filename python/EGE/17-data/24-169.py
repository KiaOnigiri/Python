f=open('24-169.txt')
s=f.read()
#s='ZZZXYZXYZXZZZ'
c='XYZ'
while c in s:
    c+='XYZ'
c=c[:-3]
print(len(c))
