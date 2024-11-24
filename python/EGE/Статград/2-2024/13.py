from ipaddress import *

for maska in range(15,32+1):
    k=0
    for uz in ip_network(f'147.222.199.75/{maska}',0):
        loc=f'{uz:b}'
        if loc[:8]==loc[24:] and loc[8:16]==loc[16:24]:
            print(uz)
            k+=1
    if k>=1:
        k=0
        for uz in ip_network(f'147.222.199.75/{maska}',0):
            loc=f'{uz:b}'
            if loc.count('1')==14:
                k+=1
    print(f'Маска={maska}; Кол-во={k}')
