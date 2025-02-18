b='175.122.144.0'
d=[]
for x in b.split('.'):
    d.append('0'*(8-len(bin(int(x))[2:]))+bin(int(x))[2:])
print('.'.join(d))
