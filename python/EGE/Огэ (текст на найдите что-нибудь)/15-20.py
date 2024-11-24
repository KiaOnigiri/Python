b=[]
while True:
    r=int(input())
    if r==0:
        break
    if r%2==0 and str(r)[-1]!='2':
        b.append(r)
    
print(min(b))
