from ipaddress import *
def bin8(x):
    x=bin(x)[2:]
    x='0'*(8-len(x))+x
    return x

k=0
Mersenn=[(2**i)-1 for i in range(1,9)]
print(Mersenn)
for x in ip_network('139.75.100.0/255.255.252.0',0):
    x=x.compressed.split('.')
    #x=[bin8(int(y)) for y in x]
    if int(x[3]) in Mersenn:
        k+=1
        print(x)
print(k)
