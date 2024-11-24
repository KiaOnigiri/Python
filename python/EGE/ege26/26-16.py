f=open('26-16.txt')
s=f.read().splitlines()
space,c=[int(z) for z in s[0].split()]
s=s[1:]
s=[int(z) for z in s]
s.sort()
k=0
for i in range(len(s)):
    if k+s[i]>space:
        break
    k+=s[i]
#print(space-k,k)
for j in range(i,i+200):
    print(s[j],s[j]-s[i-1])
