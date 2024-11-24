f=open('26-89.txt')
s=f.read().splitlines()
n=int(s[0])
s=s[1:]
s=[int(z) for z in s]
s.sort(reverse=True)
box=[s[0]]
for i in range(1,len(s)):
    if box[-1]-s[i]>=3:
        box.append(s[i])
print(len(box),box[-1])
