for n in range(1,101):
    r=bin(n)[2:]
    if n%4==0:
        r+='00'
    if n%4==1:
        r+='01'
    if n%4==2:
        r+='10'
    if n%4==3:
        r+='11'
    if int(r,2)<100:
        print(int(r,2))
#96
