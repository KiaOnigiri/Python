n = int(input())
time = int(input())

fields = []
for _ in range(n):
    fields.append(int(input()))
    fields.append(time)
fields=fields[:-1]
g=sum(fields)/2
k=0
m=0
l=0
for i in range(len(fields)):
    k+=fields[i]
    if k==g:
        break
    elif k>g:
        m=k-int(g)
        l=i
        break
if l%2!=0:
    print(int(int(g)+m)-min(k-sum(fields[:l]),k-sum(fields[l+1:])))
else:
    print(int(int(g)+m))
