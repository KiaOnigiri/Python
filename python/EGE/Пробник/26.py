f=open('C:/python/EGE/Пробник/26 вар1.txt')
s=f.read().splitlines()
s=[[int(y) for y in x.split()] for x in s]
s=[[x[0],x[0]+x[1]] for x in s]
s.sort(key = lambda x: x[1])
#print(max([x[0]+x[1] for x in s]))
#2658
b=[s[0]]
for x in s:
    if b[-1][1]<=x[0]:
        b.append(x)
print(len(b),b[-2],b[-1])
s.sort()
print(s[-5:])
