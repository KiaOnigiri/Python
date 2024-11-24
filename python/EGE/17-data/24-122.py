f=open('24-4.txt')
s=f.read()
k=1
kmin=0
ip=0
r=0
for i in range(1,len(s)):
    if s[i-1]>s[i]:
        k+=1
        if k>kmin:
            kmin=k
            ip=i-kmin+2
    else:
        k=1
'''
for j in range(1,len(s)):
    if s[j-1]>s[j]:
        r+=1
        if r==kmin:
            ip=j-kmin+2
            
    else:
        r=1
'''
        
print(ip)
