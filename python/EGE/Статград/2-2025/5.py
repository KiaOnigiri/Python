for n in range(1,134217759+1):
    r=bin(n)[2:]
    r=bin(r.count('1'))[2:]+bin(r.count('0'))[2:]
    r=int(r,2)
    if r==214:
        print(n,r)
b=bin(214)[2:]
for i in range(len(b)-1):
    if b[i+1]=='0':
        continue
    ones=b[:i+1]
    zeroes=b[i+1:]
    onesd=int(ones,2)
    zeroesd=int(zeroes,2)
    print(ones,zeroes,onesd,zeroesd)
print(int('1'+'0'*22+'1'*5,2))
