def fromAny(x,y):
    ans=0
    for i in range(len(x)):
        n=x[i]
        if x[i].isdigit()==False:
            n=ord(x[i])-ord('A')+10
        n=int(n)
        ans+=n*y**(len(x)-i-1)
    return ans


for x in range(0,37):
    n=x
    if n>=10:
        n=chr(ord('A')+n-10)
    if (fromAny(f'F29{n}8EAD6',37)*fromAny(f'BA{n}DE0C1B',37))%36==0:
        print(fromAny(f'1{n}2',37))
#2703
