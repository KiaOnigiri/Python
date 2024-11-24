b=[]
for i in range(333666,666999):
    if i%17==0 and str(i).count('7')>=2:
        b.append(i)
print(max(b),len(b))
