f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/Пробник/01-2025/files/24_19254.txt')
s=f.read()
#s='aaFSRQaaaFSRQaFSRQaaaaa'
s=s.split('FSRQ')
s=[len(x) for x in s]
#s=[1]*81
b=[]
k=80
for i in range(len(s)-k):
    b.append(sum([s[i+j] for j in range(0,k+1)]))
#print()
print(max(b)+4*k+6)
