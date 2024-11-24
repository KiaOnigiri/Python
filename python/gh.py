from itertools import *
b=[]
for x1 in '123456':
    for x2 in '123456':
        for x3 in '123456':
            for x4 in '123456':
                for x5 in '123456':
                    for x6 in '123456':
                        x=x1+x2+x3+x4+x5+x6
                        if len(set(list(x)))==len(list(x)) and '21' not in x:
                            b.append(x)
print(len(set(b)))
