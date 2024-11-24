def isCube(x):
    d=round(x**(1/3))
    return d**3==x


f=open('9-178.txt')
s=f.read().splitlines()
s=[[int(y) for y in x.split('\t')] for x in s]
k=0
for x in s:
    if len(set(x))!=3:
        continue
    if isCube(x[0]*x[1]) or isCube(x[2]*x[1]) or isCube(x[0]*x[2]):
        k+=1
        print(x)
print(k)
