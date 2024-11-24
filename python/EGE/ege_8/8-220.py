a='СОТКАПЛЗ'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    x=x1+x2+x3+x4+x5
                    if x5!='О' and x5!='А' and 'ЗЛО' not in x and len(set(x))==len(x):
                        
                        k+=1
print(k)
