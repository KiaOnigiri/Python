f=open('26-97.txt')
s=f.read().splitlines()
n=int(s[0])
s=s[1:]
s=[[int(x) for x in z.split()] for z in s]
s.sort(reverse=True, key=lambda x: x[0]-2*x[1])
b=[s[0]]
for i in range(1, len(s)):
    if (b[-1][0]-b[-1][1]*2)-(s[i][0])>=3:
        b.append(s[i])
print(len(b),b[-1][0])
print(b[-2])
