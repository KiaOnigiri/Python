def allchet(x):
    for j in str(x):
        if j in '13579':
            return False
    return True
def allnechet(x):
    for j in str(x):
        if j in '02468':
            return False
    return True


f=open('../17-363.txt')
s=f.read().splitlines()
s=[int(z) for z in s]
smx=max([z for z in s if allnechet(z)])

k=[]
for i in range(len(s)-1):
    if (allchet(s[i]) and s[i]+s[i+1]>smx) or (allchet(s[i+1]) and s[i]+s[i+1]>smx):
        k.append(s[i]+s[i+1])
print(len(k),max(k))
