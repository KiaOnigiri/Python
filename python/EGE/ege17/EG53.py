b=[]
for i in range(10,1178+1):
    r=[int(j) for j in str(i)]
    if r[-1]!=0 and r[-1]!=2 and r[-1]!=6 and r[-1]!=8 and i%2==0:
        if r[-1]!=4:
            b.append(i)
        else:
            if r[-2]!=1:
                b.append(i)
print(sum(b),min(b))        
