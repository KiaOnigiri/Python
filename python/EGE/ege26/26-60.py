f=open('26-60.txt')
s=f.read().splitlines()
k,n=s[0].split()
s=s[1:]
s_ColvoAbiturNaSpet=[]
s_Abitur=dict()
b=[]
for i in range(len(s)):
    r=s[i].split()
    #print(r)
    if len(r)==2:
        ball=int(r[0])
        n_spec=int(r[1])
        if s_Abitur.get(n_spec):
            s_Abitur[n_spec].append(ball)
        else:
            s_Abitur[n_spec]=[ball]
    else:
        s_ColvoAbiturNaSpet.append(int(r[0]))
        if int(r[0])==150:
            b.append(i)
#print(s_ColvoAbiturNaSpet[:5])
#print(list(s_Abitur.items())[:5])
t=0
mx=0
kmx=-200
mn=1000
for k,v in s_Abitur.items():
    konkurs=len(s_Abitur[k])
    s_Abitur[k].sort(reverse=True)
    t+=min(konkurs,s_ColvoAbiturNaSpet[k])
    if k in b:
        mn=min(mn, s_Abitur[k][min(konkurs,s_ColvoAbiturNaSpet[k])-1])
    if konkurs/s_ColvoAbiturNaSpet[k]>=mx:
        mx=konkurs/s_ColvoAbiturNaSpet[k]
        kmx=k
        #print(kmx,mx)
print(mx,kmx,s_ColvoAbiturNaSpet[kmx],s_Abitur[15][24])
#print(s_ColvoAbiturNaSpet.count(150))
print(t)
#print(t,)
#print(s_Abitur[6][149])
'''
for x in s_Abitur:
    if len(d)<s_ColvoAbiturNaSpet[x[1]]:
        '''
