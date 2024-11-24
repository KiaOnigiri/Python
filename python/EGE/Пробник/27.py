f=open('C:/python/EGE/Пробник/27v01_B.txt')
s=f.read().splitlines()
k=s[0]
n=s[1]
s=s[2:]
s=[int(x) for x in s]
t=list(sorted(s))
ans=t[6]
#s.remove(ans)
print(s.index(ans),ans)
#292300 3802904
#292299 3802905
#292298 3802906
#261100 3802934
#292301 3802939
#323504 3802939
print(k)
#31201
#96472 3803027
