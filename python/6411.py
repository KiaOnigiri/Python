s='ЕСТВО'
s1='ЕО'
k=0
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    for x6 in s:
                        for x7 in s:
                            for x8 in s:
                                t=x1+x2+x3+x4+x5+x6+x7+x8
                                if t.count('Е')+t.count('О')>=3 and t.count('С')+t.count('Т')+t.count('В')>=4 and 'ЕЕ' not in t and 'ОО' not in t and 'ЕО' not in t and 'ОЕ' not in t:
                                    k+=1
print(k)
