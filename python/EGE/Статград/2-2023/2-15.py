for a in range(1000):
    b=[]
    for x in range(40000):
        if (((x&57>0) or (x&99>0))<=(x&a>0)):
            b.append(1)
        else:
            b.append(0)
    if sum(b)==len(b):
        print(a)
        break
#123
