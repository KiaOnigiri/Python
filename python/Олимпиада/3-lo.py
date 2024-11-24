def prime(x):
  for y in range(2,int(x**0.5)+1):
    if x%y==0:
      return False
  return True
          

x,y,z=[int(q) for q in input().split()]
n=int(input())
sk=[]
for i in range(n):
  e1,e2=input().split()
  e2=int(e2)
  sk.append([e1,e2])



dots=[]
for k in sk:
  if k[0]=='x':
    x+=k[1]
  if k[0]=='y':
    y+=k[1]
  if k[0]=='z':
    z+=k[1]
  dots.append((x,y,z))
  
kol=0
dots=list(set(dots))
for d in dots:
  if prime(abs(d[0])+abs(d[1])+abs(d[2])):

    kol+=1
    
print(kol)
