from ipaddress import *
def bin8(x):
    x=bin(x)[2:]
    x='0'*(8-len(x))+x
    return x

k=0
for x in ip_network('211.48.136.64/27',0):
    x=x.compressed.split('.')
    x=[bin8(int(y)) for y in x]
    if x[3][-2:]=='11':
        k+=1
        print(x)
print(k)
    
