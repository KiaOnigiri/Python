from fnmatch import fnmatch
f=open('24_314.txt')
s=f.read()
#s='SMDTSMDTSMDTSMDTM'
s=s.split('TS')
k=0
kmax=0
b=[]
for i in range(len(s)-1):
    if fnmatch(s[i][-3:],'S??') and len(s[i+1])==2:
        k=7
    elif k>=7 and len(s[i+1])==2 and len(s[i])==2:
        k+=4
    elif k>=7 and len(s[i])==2 and fnmatch(s[i+1][:3],'??T'):
        k+=5
        kmax=max(kmax,k)
        k=0
    else:
        k=0
print(kmax)
        
