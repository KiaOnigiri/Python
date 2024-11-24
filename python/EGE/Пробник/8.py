s='ФАВОРИТ'
k=1
ans=0
for x in 'ФАВРИТ':
    for x1 in s:
        for x2 in s:
            for x3 in s:
                for x4 in s:
                    for x5 in s:
                        sk=x+x1+x2+x3+x4+x5
                        if sk.count('Р')==2 and k%2==0:
                            ans+=1
                        k+=1
print(ans)
