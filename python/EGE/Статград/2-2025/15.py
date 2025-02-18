p=range(153697,780411+1)
q=range(275071,904082+1)
r=range(722050,984086+1)
a=[]
b=[]
for x in range(150000,985000):
    f=(not(x in a))<=(((x in p)==(x in q))<=((x in r)==(x in q)))
    if f==0:
        b.append(x)
print(max(b),min(b),max(b)-min(b))
#709015
