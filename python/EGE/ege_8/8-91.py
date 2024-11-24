a='КАЛИЙ'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    c=x1+x2+x3+x4+x5
                    if len(set(c))==len(c) and x1!='Й' and 'ИА' not in c:
                        k+=1
print(k)
