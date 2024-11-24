import time
t1=time.time()
n=int(input())
k=0
for x1 in range(n//50+1):
    for x2 in range(n//100+1):
        for x3 in range(n//200+1):
            c=x1*50+x2*100+x3*200
            if c==n:
                k+=1
print(k)
t2=time.time()
print(str(t2-t1))
