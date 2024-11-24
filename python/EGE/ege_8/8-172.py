a='КОРНЕТ'
k=0
b=[]
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    x=x1+x2+x3+x4+x5
                    if x.count('Е')<=1 and x.count('О')<=1:
                        b.append(x)
                            
print(len(list(set(b))))
