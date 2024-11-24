def inAny(x,y):
    b=[]
    while x>0:
        ost=x%y
        if ost>9:
            ost=chr(ord('A')+ost-10)
        b.append(str(ost))
        x//=y
    b.reverse()
    return ''.join(b)

#print(inAny(24,25))
ans=inAny(3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2025,25)
print(ans)
#10
print(ans.count('0'))
