k=0
for N in range(1,101):
    b=bin(N)[2:]
    b+=str(b.count('1')%2)
    b+=str(b.count('1')%2)
    R=int(b,2)
    if R in [i for i in range(20,50+1)]:
        k+=1
        print(N,R)
print(k)
