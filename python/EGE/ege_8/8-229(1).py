s='0123456'
k=0
for x1 in '1246':
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    for x6 in s:
                        for x7 in s:
                            x=x1+x2+x3+x4+x5+x6+x7
                            if '22' in x and '44' in x:
                                continue
                            else:
                                k+=1
print(k)
