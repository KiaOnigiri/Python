def prime(x):
    for y in range(2,int(x**0.5)+1):
        if x%y==0:
            return False
    return True

b=[]
for n in range(32):
    for m in range(32):
        for k in range(32):
            s='0'+'3'*n+'4'*m+'3'*k+'0'
            while '00' not in s:
                s=s.replace('033','21120',1)
                s=s.replace('034','22120',1)
                s=s.replace('04','220',1)
                s=s.replace('030','100',1)
            if len(s)==65:
                sm=sum([int(x) for x in s])
                if prime(sm):
                    b.append([n+k,len(s),sm,n,m,k])
b.sort()
print(b[:5])
