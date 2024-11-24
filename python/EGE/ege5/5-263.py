k=0
for N in range(2,1000):
    if N%2==0:
        N=N//2
    else:
        N-=1
    if N%3==0:
        N=N//3
    else:
        N-=1
    if N%7==0:
        N=N//7
    else:
        N-=1
    if N==2:
        k+=1
print(k)
