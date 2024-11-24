s='ТИМАШЕВСК'
s2='ТМШВСК'
k=0
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    for x6 in s:
                        for x7 in s:
                            for x8 in s:
                                for x9 in s:
                                    t=[x1,x2,x3,x4,x5,x6,x7,x8,x9]
                                    t1=x1+x2+x3+x4+x5+x6+x7+x8+x9
                                    if x1 in s2 and x9 in s2 and len(set(t))==len(t) and ('ИАЕ' in t1 or 'ИЕА' in t1 or 'ЕАИ' in t1 or 'ЕИА' in t1 or 'АЕИ' in t1 or 'АИЕ' in t1):
                                        k+=1
print(k)

