c='zzAzBzzAzzzzBzzzBzAzz'
'''
f=open('24.txt')
c=f.read()
b=[]
for i in range(len(c)):
    fa=False
    fb=False
    for j in range(i,len(c)):
        if fa==True and c[j]=='A' or fb==True and c[j]=='B':
            break
        elif c[j]=='A':
            fa=True
        elif c[j]=='B':
            fb=True
    if fa and fb:
        b.append(j-i)
print(max(b))
'''
cA=[x for x in c.split('A')]
cB=[[y for y in x.split('B')] for x in cA]
cB=[[len(y) for y in x] for x in cB]
h=[]
for i in range(len(cB)-1):
    if len(cB[i])==1 and len(cB[i+1])==1:
        continue
    if len(cB[i])==2 and len(cB[i+1])==1:
        h.append(sum(cB[i])+cB[i+1][0])
    elif len(cB[i])==1 and len(cB[i+1])==2:
        h.append(cB[i][0]+cB[i+1][0]+cB[i+1][1])
    elif len(cB[i])>2 and len(cB[i+1])==1:
        h.append(cB[i][-2]+cB[i][-1]+cB[i+1][0])
    elif len(cB[i])==1 and len(cB[i+1])>2:
        h.append(cB[i][-1]+cB[i+1][1]+cB[i+1][0])
    elif len(cB[i])>2 and len(cB[i+1])>2:
        h.append(cB[i][-1]+cB[i+1][1]+cB[i+1][0])
        h.append(cB[i][-2]+cB[i][-1]+cB[i+1][0])
print(h)
