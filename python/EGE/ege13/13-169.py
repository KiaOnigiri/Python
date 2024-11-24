from ipaddress import *
def bin8(x):
    x=bin(x)[2:]
    x='0'*(8-len(x))+x
    return x

k=0
for x in ip_network('117.32.0.0/255.224.0.0',0):
    x=x.compressed.split('.')
    #x=[bin8(int(y)) for y in x]
    if len(set(x))==3 and x!=['117','32','0','0'] and x!=['117','63','255','255']:
        k+=1
        #print(x)
print(k)
#40638
#00100000.00000000.00000000
