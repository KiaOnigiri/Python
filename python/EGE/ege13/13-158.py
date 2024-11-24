from ipaddress import *
def bin8(x):
    x=bin(x)[2:]
    x='0'*(8-len(x))+x
    return x

k=0
for x in ip_network('192.168.248.176/255.255.255.240',0):
    x=x.compressed.split('.')
    x=[bin8(int(y)) for y in x]
    if ''.join(x).count('1')>''.join(x).count('0'):
        k+=1
        print(x)
print(k)
#1
