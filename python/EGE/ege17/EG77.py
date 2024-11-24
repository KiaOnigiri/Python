import math
def min3(x):
    if min(x) in x[0:2+1]:
        return 'yes'
    return 'no'


b=[]
for i in range(2020,647038+1):
    i=str(i)
    i=[int(z) for z in i]
    if sum(i)<10 and min3(i)=='no':
        b.append(''.join([str(p) for p in i]))
k=1000000
b=[int(c) for c in b]
sr_ar=sum(b)/len(b)
for m in b:
    if abs(sr_ar - m)<k:
        k=abs(sr_ar - m)
        o=m
print(len(b),o)
