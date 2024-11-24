def Win(x):
    if x+1>=96:
        return True
    if x%3==0:
        if 96<=x+x//3:
            return True
    if x%2==0:
        if 96<=x+x//2:
            return True
    if x%2!=0 and x%3!=0:
        if 96<=x*2:
            return True
    return False


b=[]
for x in range(1,95+1):
    p=[x+1]
    if x%3==0:
        p.append(x+x//3)
    if x%2==0:
        p.append(x+x//2)
    if x%2!=0 and x%3!=0:
        p.append(x*2)
    pw=[1 for y in p if y>=96]
    if len(pw)>0:
        continue
    k1=[1 for y in p if Win(y)]
    if len(k1)==len(p):
        b.append(x)
g=[]
for i in range(1,100):
    if i+1>=96 or (i%3==0 and (i+i//3)>=96) or (i%2==0 and (i+i//2)>=96) or (i%2!=0 and i%3!=0 and i*2>=96):
        continue
    if (i+i//2) in b and i%2==0:
        g.append(i)
    if (i+i//3) in b and i%3==0:
        g.append(i)
    if (i*2) in b and i%3!=0 and i%2!=0:
        g.append(i)
    if i+1 in b:
        g.append(i)
g=sorted(set(g))
print(g[-1], g[-2], g, b)
'''
for i in range(1,100):
    if '''
