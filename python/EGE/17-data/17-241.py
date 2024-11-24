f=open('17-1.txt')
s=f.read().splitlines()
s=[int(z) for z in s]
sr_ar=sum(s)/len(s)
q=0
k=0
b=[]
for i in range(1,len(s)-1):
    if s[i-1] < sr_ar:
        q+=1
    if s[i] < sr_ar:
        q+=1
    if s[i+1] < sr_ar:
        q+=1
    if '5' in str(s[i-1]):
        k+=1
    if '5' in str(s[i]):
        k+=1
    if '5' in str(s[i+1]):
        k+=1
    if q>=2 and k>=2:
        b.append(s[i+1]+s[i]+s[i-1])
    q=0
    k=0
print(len(b),max(b))
