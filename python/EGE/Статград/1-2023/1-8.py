def ege8():
    b='ABECT'
    a=1
    for x1 in b:
        for x2 in b:
            for x3 in b:
                for x4 in b:
                    for x5 in b:
                        #print(f'{a}. {x1},{x2},{x3},{x4},{x5}')
                        a+=1
                        if x1+x2+x3+x4+x5=='CBETA':
                            return a
                        
                        
print(ege8())
