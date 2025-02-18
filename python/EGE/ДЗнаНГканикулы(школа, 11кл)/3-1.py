chet='02468AC'
nechet='13579B'
cnt=0
for x1 in chet[1:]:
    for x2 in nechet:
        for x3 in chet:
            for x4 in nechet:
                for x5 in chet:
                    for x6 in nechet:
                        for x7 in chet:
                            x=x1+x2+x3+x4+x5+x6+x7
                            if x.count('2')==1:
                                cnt+=1
cnt1=0
for x1 in nechet:
    for x2 in chet:
        for x3 in nechet:
            for x4 in chet:
                for x5 in nechet:
                    for x6 in chet:
                        for x7 in nechet:
                            x=x1+x2+x3+x4+x5+x6+x7
                            if x.count('2')==1:
                                cnt1+=1
print(cnt+cnt1)
#303264
