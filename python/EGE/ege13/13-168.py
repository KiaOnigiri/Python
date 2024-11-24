from ipaddress import *
def bin8(x):
    x=bin(x)[2:]
    x='0'*(8-len(x))+x
    return x

k=0
for x in ip_network('216.130.64.0/18',0):
    x=x.compressed.split('.')
    #x=[bin8(int(y)) for y in x]
    if all([int(u)%2==0 for u in x]) and x!=['216','130','64','0']:
        k+=1
print(k)
