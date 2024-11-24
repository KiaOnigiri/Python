def calc_result(ID):
    time=d[ID][0]
    prcss=d[ID][1]
    if prcss==[0]:
        return time
    else:
        mx=[]
        for x in prcss:
            if it.get(x)==None:
                mx.append(calc_result(x))
            else:
                mx.append(it[x])
        it[ID]=time+max(mx)
        return it[ID]


f=open('22-43.txt')
s=f.read().splitlines()
s=s[1:]
s=[i.split('\t')[:-1] for i in s]
d={}
for i in range(len(s)):
    c=s[i][2].replace('"','')
    c=c.split(';')
    c=[int(x) for x in c]
    s[i]=[int(s[i][0]),int(s[i][1]),c]
    d[s[i][0]]=[s[i][1],s[i][2]]
it={}
for k,v in d.items():
    it[k]=calc_result(k)
print(max(it.values()))
