def dels(x):
    b=[]
    for i in range(1,x+1):
        if x%i==0:
            b.append(i)
    return b

print(dels(12))
for m in range(0,1000):
    s='>'+'1'*22+'2'*m+'3'*23
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s=s.replace('>1','2>',1)
        if '>2' in s:
            s=s.replace('>2','21>',1)
        if '>3' in s:
            s=s.replace('>3','11>',1)
    if sum([int(z) for z in s[:-1]])>2023:
        print(m)