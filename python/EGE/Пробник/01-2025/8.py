alph='АВНРЬЯ'
k=1
ans=0
ans1=''
for x1 in alph:
    for x2 in alph:
        for x3 in alph:
            for x4 in alph:
                for x5 in alph:
                    x=x1+x2+x3+x4+x5
                    if x1!='Я' and x.count('Ь')<=1 and 'ЯЯ' not in x:
                        ans=k
                        ans1=x

                    k+=1
print(ans,ans1)
                    
