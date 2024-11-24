c=[]
for n in '0123456789':
    for m in '0123456789':
        for x in 'm0123456789':
            for x1 in 'm0123456789':
                for x2 in 'm0123456789':
                    sx=x+x1+x2
                    sx=sx.replace('m','')
                    chislo=f'1{sx}34{n}5{m}9'
                    if int(chislo)%31007==0:
                        c.append([int(chislo),int(chislo)//31007])
for x in list(sorted(c)):
    print(f'{x[0]} {x[1]}')

