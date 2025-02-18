f=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var13-17.txt')
s=f.read()
mx=0
curr=1
for i in range(len(s)-1):
    if s[i]>=s[i+1]:
        curr+=1
    if mx<curr:
        mx=curr
    if s[i]<s[i+1]:
        curr=1
print(mx)
#19
