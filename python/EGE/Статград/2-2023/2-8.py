cht='2468'
ncht='1357'
k=0
for x1 in ncht:
    for x2 in cht:
        for x3 in ncht:
            for x4 in cht:
                for x5 in ncht:
                    for x6 in cht:
                        for x7 in ncht:
                            for x8 in cht:
                                for x9 in ncht:
                                    for x10 in cht:
                                        for x11 in ncht:
                                            x=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11
                                            if max([x.count(y) for y in x])>4:
                                                continue
                                            k+=1
                                            print(x)
print(k)
#8200800
