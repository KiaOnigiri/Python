f=open('C:/python/EGE/Статград/2-2024/Глава первая..txt')
s=f.read()
#print(s[:20])
alpha=dict()
k=0
for i in range(1,len(s)-2):
  if s[i] in 'яЯ' and s[i-1]=='-' and s[i+1].isalpha()==True and s[i+2].isalpha()==True:
    print(s[i-5:i+7])
    k+=1
print(alpha,k)
rep=dict()
for i in range(1,len(s)):
  if s[i] in 'яЯ' and s[i-1].isalpha()==False and s[i+1].isalpha()==True and s[i+2].isalpha()==True:
    rep[s[i-1]]=rep.get(s[i-1],0)+1
print(*rep.items(),sep='\n')

#[-]<[Яя][А-яЁё]{2;}>
