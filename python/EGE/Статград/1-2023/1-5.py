k=0
for n in range(34500000,45500000+1):
    r=bin(n)[2:]
    r+='0'*(2-len(bin(n%3)[2:]))+bin(n%3)[2:]
    r=r+'0'*(3-len(bin(int(r,2)%5)[2:]))+bin(int(r,2)%5)[2:]
    g=int(r,2)
#45500000
    if 1111111110<=g<=1444444416:
        k+=1
print(k,g)
