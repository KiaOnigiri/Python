a='ЗЕРКАЛО'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in a:
                        x=x1+x2+x3+x4+x5+x6
                        if x.count('З')<=1 and x.count('Е')<=1 and x.count('Р')<=1 and 0<x.count('К')<=4 and x.count('А')<=1 and x.count('Л')<=1 and x.count('О')<=1:
                            k+=1
print(k)                            
