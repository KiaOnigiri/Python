c=[]
for i in range(3905,7998+1):
    i=str(i)
    if i[-2]!='0' and i[-2]!='5' and 2<=int(i[-3])<=6:
        c.append(i)
print(len(c),min(c))
