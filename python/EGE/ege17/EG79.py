def dels(x):
    b=[1,x]
    for j in range(2,int(x**0.5)+1):
        if x%j==0:
            if j==x//j:
                b.append(j)
            else:
                b.append(j)
                b.append(x//j)
    return b


a=[]
for i in range(2095, 19402+1):
    if len(dels(i))==2 and str(i)[0]>str(i)[-1]:
        a.append(i)
k=0
for j in a:
    if str(j)[-2:]=='21' and j>k:
        k=j
print(len(a),k)
