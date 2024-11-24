f=open("17-2.txt")
c=f.read().splitlines()
c=[int(z) for z in c]
mx=max(c)
print(c.count(mx),c.index(mx)+1)
    
