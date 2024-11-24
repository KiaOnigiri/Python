a='ПЕСКАРЬ'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in a:
                        for x7 in a:
                            x=x1+x2+x3+x4+x5+x6+x7
                            if len(x)==len(set(x)) and x1!='Ь' and 'ЬЕ' not in x and 'ЬА' not in x and 'ЬР' not in x:
                                k+=1
                                
print(k)
