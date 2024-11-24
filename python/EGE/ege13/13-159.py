from ipaddress import *
def bin8(x):
    x=bin(x)[2:]
    x='0'*(8-len(x))+x
    return x

k=0
for x in ip_network('158.132.161.128/255.255.255.128',0):
    x=x.compressed.split('.')
    x=[bin8(int(y)) for y in x]
    if ''.join(x)[-1]=='1':
        k+=1
        print(x)
print(k)
#64
