b=[]
for i in range(10,9999+1):
    s=bin(i)[2:]
    if s.count('0')==5 and i%2==1 and i%3==0 and i%11==0:
        b.append(i)
print(len(b),max(b))
