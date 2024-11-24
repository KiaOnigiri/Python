'''
a='АЗИМУТ'
b=[]
for x1 in a:
    for x2 in a:
        for x3 in a:
            for x4 in a:
                for x5 in a:
                    for x6 in a:
                        
                        x=x1+x2+x3+x4+x5+x6
                        if x.count('З')+x.count('М')+x.count('Т')>=3:
                            b.append(x)

print(len(set(b)))
print(len(b))
print(b)
'''
print(int('130424',5))
