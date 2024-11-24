n=int(input())
s=[]
for i in range(n):
  s.append(int(input()))
s.sort(reverse=True)
res=s[:4]
print(*res,sep='')
