from ipaddress import *
def bin8(x):
    x=bin(x)[2:]
    x='0'*(8-len(x))+x
    return x

k=0
for x in ip_network('202.75.38.152/255.255.255.248',0):
    x=x.compressed.split('.')
    x=[bin8(int(y)) for y in x]
    if '111' in ''.join(x):
        k+=1
        print(x)
print(k)
#4
