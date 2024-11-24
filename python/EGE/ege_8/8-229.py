q=[]
c='0123456'
for x1 in c:
    for x2 in c:
        for x3 in c:
            for x4 in c:
                for x5 in c:
                    for x6 in c:
                        for x7 in c:
                            x=x1+x2+x3+x4+x5+x6+x7
                            if x1!='0' and x1!='3' and x1!='5' and ('22' not in x or '44' not in x):
                                q.append(x)
print(len(set(q)))
