def word(x):
    if x>=10:
        x=chr(ord('A')+x-10)
    return x


k,d=map(int,input().split())
c=0
    
for x1 in range(d-1,5-1,-1):
    for x2 in range(x1-1,0-1,-1):
        for x3 in range(x2-1,0-1,-1):
            for x4 in range(x3-1,0-1,-1):
                for x5 in range(x4-1,0-1,-1):
                    for x6 in range(x5-1,0-1,-1):
                        sx=str(word(x1))+str(word(x2))+str(word(x3))+str(word(x4))+str(word(x5))+str(word(x6))
                        #print(sx,int(sx,d))
                        if int(sx,d)%k==0:
                            c+=1
print(c)
