def again(x):
    x=str(x)
    for symbol in x:
        if x.count(symbol)>1:
            return 'yes'
    return 'no'

def power3(x):
    k=1
    while k<x:
        k*=3
    if x==k:
        return 'yes'
    else:
        return 'no'


b=[]
for i in range(138,603884+1):
    if again(i)=='yes' and power3(i)=='yes':
        b.append(i)

mxs=0
for j in b:
    s=sum([int(z) for z in str(j)])
    if s>mxs:
        mxs=s
for j in b:
    s=sum([int(z) for z in str(j)])
    if s==mxs:
        mn=j
        break
print(len(b),mn)
