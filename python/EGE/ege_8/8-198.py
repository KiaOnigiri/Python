a='АБВГД'
k=0
for x1 in a:
    for x2 in a:
        for x3 in a:
            x=x1+x2+x3
            xd=list(x)
            if sorted(x)==xd:
                print(x)
                k+=1
print(k)
