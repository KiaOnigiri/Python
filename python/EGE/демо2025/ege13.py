from ipaddress import *
k=0
for x in ip_network('172.16.168.0/255.255.248.0',0):
    x=f'{x:b}'
    if x.count('1')%5!=0:
        k+=1
print(k)
#1663
