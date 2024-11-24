f=open('26-78.txt')
s=f.read().splitlines()
n,t1,t2=[int(z) for z in s[0].split()]
s=s[1:]
s=[[int(x) for x in z.split()] for z in s]
s.sort()
t_end=0
k=0
for x in s:
    if x[0]<=t1:
        t_end=max(x[1],t_end)
        if t_end>t2:
            k+=1
            print(t_end,k)
            break
    else:
        k+=1
        print(t_end)
        t1=t_end
