k=0
while True:
    r=int(input())
    if r==0:
        break
    if r%7==0 and r<=1000:
        continue
    else:
        k+=1
if k==0:
    print('YES')
else:
    print('NO')
