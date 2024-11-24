n=6
a=[2,0,2,5,7,4]
q=5
zap=['2 13','2 0','2 11','2 28','2 29','2 1000']
for i in zap:
    com=i.split()
    com=[int(j) for j in com]
    if com[0]==1:
        a[com[1]-1]=com[2]
    elif com[0]==2:
        z=com[1]
        baseOr=0
        for x in a:
            baseOr|=x
        print(baseOr,z)
        for x in range(z,0-1,-1):
            if baseOr&x==baseOr:
                break
        if x==0:
            print(x)
        else:
            print(x+1)
        '''k=(baseOr+1)&z
        for x in range(z,0-1,-1):
            if (x-k)%()==0:
                print(x-k,x)
                break'''
        '''for x in range(0,z+1):
            if (baseOr|x)<=z:
                k+=1'''
        #print(k)
