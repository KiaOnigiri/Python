letters='ABETUY'
numbers='0011!'
a=set()
for x1 in letters:
    for x2 in letters:
        for x3 in letters:
            for x4 in letters:
                for x5 in letters:
                    for x6 in letters:
                        for x7 in numbers:
                            for x8 in numbers:
                                for x9 in numbers:
                                    for x10 in numbers:
                                        for x11 in numbers:
                                            x=[x1,x2,x3,x4,x5,x6]
                                            g=x7+x8+x9+x10+x11
                                            if len(set(x))==len(x) and g.count('0')==2 and g.count('1')==2:
                                                a.add(x1+x7+x2+x8+x3+x9+x4+x10+x5+x11+x6)
print(len(a))
