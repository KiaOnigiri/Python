f=open('09.txt')
s=f.read().splitlines()
s=[[int(x) for x in j.split()] for j in s]
#print(s[:20])
k=0
for y in s:
    y=sorted(y)
    if len(set(y))==len(y):
        if (y[0]+y[5])/2>(y[1]+y[2]+y[3]+y[4])/4:
            k+=1
print(k)
