def dels(x):
    b=[1,x]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            b.append(i)
            b.append(x//i)
    return sorted(set(b))


print(dels(17))
for n in range(0,1000):
    s='>'+16*'1'+n*'2'+16*'3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s=s.replace('>1','1>',1)
        if '>2' in s:
            s=s.replace('>2','>3',1)
        if '>3' in s:
            s=s.replace('>3','>1',1)
    k=sum([int(h) for h in s[:-1]])
    if dels(k)==[1,k]:
          print(n,k)
#5
