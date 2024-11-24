b=[]
for i in range(7525,13486+1):
    if i%7==0 and i%6!=0 and i%9!=0 and i%14!=0 and i%21!=0:
        b.append(i)
print(len(b),min(b))
