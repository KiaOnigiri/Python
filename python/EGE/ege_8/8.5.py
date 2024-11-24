c='ПЯТНИЦА'
k=0
for x1 in c:
    for x2 in c:
        for x3 in c:
            for x4 in c:
                for x5 in c:
                    x=x1+x2+x3+x4+x5
                    if x.count('Я')==1 and x1!='Н':
                        k+=1
print(k)
#5616
