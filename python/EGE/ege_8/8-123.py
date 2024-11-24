a='ВОРОН'
k=0
b=[]
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    x=x1+x2+x3+x4+x5
                    if 'ОО' not in x and x.count('О')==2 and x.count('В')==1 and x.count('Р')==1 and x.count('Н')==1:
                            b.append(x)

print(len(set(b)))
