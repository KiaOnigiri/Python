f=open('26-105.txt')
s=f.read().splitlines()
n,k=s[0].split()
n=int(n)
k=int(k)
s=s[1:]
s=[int(z) for z in s]
s.sort()
print(s[:5])
print(n,k)
for q in range(100,len(s)):
    goods=s[:q]
    k_sale=len(goods)//6
    goods=goods[:-k_sale]+[z*0.5 for z in goods[-k_sale:]]
    if k-sum(goods)<=0:
        break
    else:
        print(sum(goods),len(goods),k-sum(goods))
#470 20
