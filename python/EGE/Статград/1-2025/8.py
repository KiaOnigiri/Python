k=0
for x1 in '123456789ABCDE':
    for x2 in '0':
        for x3 in '0':
            for x4 in '123456789ABCDE':
                for x5 in '123456789ABCDE':
                    for x6 in '123456789ABCDE':
                        for x7 in '123456789ABCDE':
                            for x8 in '123456789ABCDE':
                                x=x1+x2+x3+x4+x5+x6+x7+x8
                                if x.count('A')+x.count('B')+x.count('C')+x.count('D')+x.count('E')<=4:
                                    k+=1
print(k)
print(k*(6+5+4+3+2+1))
