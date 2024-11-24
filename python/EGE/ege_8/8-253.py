a='012345678'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    x=x1+x2+x3+x4+x5
                    if x.count('3')<=1 and x1!='0' and x1!='1' and x1!='3' and x1!='5' and x1!='7' and x5!='1' and x5!='8':
                        k+=1
print(k)
