f=open('26-90.txt')
s=f.read().splitlines()
n=int(s[0])
s=s[1:]
s=[int(z) for z in s]
s.sort(reverse=True)
k=0
for i in range(2500):
    k+=s[i]/2
k+=sum(s[2500:])
print(k)
#48825239
