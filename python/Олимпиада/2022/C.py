a=list(map(int, input().split()))
b=list(map(int, input().split()))
count=int(input())
l=b
for i in range(1,count+1):
    j=list(map(int, input().split()))
    c=l[j[0]-1:j[1]-1+1]
    c.reverse()
    l=l[:j[0]-1]+c+l[j[1]:]
v=a[1]
print(l[v-1])
