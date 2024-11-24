f=open('26-45.txt')
s=f.read().splitlines()
n=int(s[0])
s=s[1:]
s=[int(z) for z in s]
s.sort()
d=dict(zip(s,s))
#print(s[:5])
k=0
mx=0
s_even=[z for z in s if z%2==0]
s_odd=[z for z in s if z%2!=0]
for i in range(n):
    for j in range(n-1, i, -1):
        if (s[i]+s[j])%2==0:
            sr_ar=(s[i]+s[j])//2
            if sr_ar in d:
                k+=1
                mx=max(mx, sr_ar)

print(k,mx)
