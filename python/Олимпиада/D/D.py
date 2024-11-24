def bliz(x,y):
    if len(x)>len(y):
        x,y=y,x
    c=1
    while c<len(x)+1:
        b=x[0:c]
        if y.find(b)==0:
            c+=1
        else:
            break
    c-=1
    x=x[c:]
    x=x[::-1]
    y=y[::-1]
    s=1
    while s<len(x)+1:
        b=x[0:s]
        if y.find(b)==0:
            s+=1
        else:
            break
    s-=1
    return c+s


#print(bliz('abcde','zzz'))
a=open('04')
a=a.read().splitlines()
print(a)
n=int(a[0])
a=a[1:]
for i in range(n):
    c=[]
    for j in range(n):
        if i==j:
            continue
        b=bliz(a[i],a[j])
        #print(a[i],b,a[j])
        c.append([b,j])
    mx=max(c)
    print(mx[1]+1,end=' ')
