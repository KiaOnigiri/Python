b=[]
for i in range(1234567,7654321+1):
    c=i
    c=str(c)
    r=int(c[:2])-int(c[-2:])
    if r==0:
        continue
    if i%r==0:
        b.append(i)
print(len(b),max(b))

