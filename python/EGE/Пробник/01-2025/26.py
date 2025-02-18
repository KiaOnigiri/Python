f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Пробник/01-2025/files/26_19256.txt')
s=f.read().splitlines()
cnt=s[0]
s=s[1:]
s=[[int(y) for y in x.split()] for x in s]
s=list(sorted(s))
b=[]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        continue
    b.append(s[i])
kmax=0
k=1
student=0
td=0
for i in range(len(b)):
    if b[i][0]==40031:
        print(td,b[i][1])
        td+=1
for i in range(len(b)-1):
    if b[i][0]==b[i+1][0] and b[i][1]+1==b[i+1][1]:
        k+=1
    else:
        if kmax<k:
            kmax=k
            student=b[i-1][0]
        k=1
print(student,kmax)
