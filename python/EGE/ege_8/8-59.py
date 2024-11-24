a='ПИРОГ'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    c=x1+x2+x3+x4+x5
                    c=[str(h) for h in c]
                    if c.count('Р')==0:
                        k+=1
                        continue
                    if c.count('Р')<=2 and(c.index('Р')+1==c.index('О') or c.index('Р')+1==c.index('И')):
                        k+=1
print(k)
