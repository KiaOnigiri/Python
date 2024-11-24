k=0
for i in range(1,35+1):
    s='1'*i
    while '111' in s:
        s=s.replace('111','33',1)
        s=s.replace('333','1',1)
    if s=='131':
        k+=1
print(k)
