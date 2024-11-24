def fromAny(x,y):
    x=x[::-1]
    g=0
    for i in range(len(x)):
        if x[i].isdigit()==False:
            c=ord(x[i])-ord('A')+10
        else:
            c=int(x[i])
        g+=c*(y**i)
    return g


a=''
for i in range(37):
    if i>=10:
        i=chr(ord('A')+i-10)
    a+=str(i)
b=[]
for x in a:
    for y in a:
        c=['1','2',x,'6','4','3',y,'7']
        k=fromAny(c,37)
        if k%36==0:
            b.append(fromAny(y+x,37))
print(max(b))
