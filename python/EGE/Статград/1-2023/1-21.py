a=[0]*26
a[3]=1
for i in range(4,25+1):
    if i==12:
        continue
    a[i]+=a[i-1]
    if i%2==0:
        a[i]+=a[i//2]
    if int(i**0.5)**2==i:
        a[i]+=a[int(i**0.5)]
print(a)
