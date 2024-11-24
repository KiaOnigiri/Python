def inAny(x,n):
  s=[]
  while x>0:
    s.append(x%n)
    x//=n
  s.reverse()
  return s

commands=[]
n=int(input())
for i in range(n):
  x=int(input())
  x12=inAny(x,12)

  for c in x12:
    if c%3==0:
      commands.append(c)

print(len(commands))
