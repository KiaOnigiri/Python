a='РУСТАМ'
k=0
b=[]
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in a:
                        
                        x=x1+x2+x3+x4+x5+x6
                        if x.count('Р')+x.count('С')+x.count('Т')+x.count('М')>=3:
                            k+=1

print(k)
