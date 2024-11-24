def unrep(x):
    return [z for z in x if x.count(z)==1]


f=open('9-176.txt')
s=f.read().splitlines()
s=[[int(z) for z in x.split('\t')] for x in s]
#print(unrep([1,1,2,2,3,4,4,4]))
k=0
for line in s:
    if len(set(line))==7:
        continue
    if sum(unrep(line))%2==1:
        k+=1
print(k)
