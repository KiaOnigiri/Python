s=open('C:/Users/snser/OneDrive/Документы/GitHub/Python/python/EGE/ege24/Сборник/Сборник_ЕГЭ24_ФАЙЛЫ/24var18-20.txt').read()
curr=s[0]
curr_num=1
mx=0
mx_curr=''
for i in range(len(s)-1):
    if s[i]<s[i+1]:
        curr_num+=1
        curr+=s[i+1]
        if mx<curr_num:
            mx=curr_num
            mx_curr=curr
    else:
        curr_num=1
        curr=s[i+1]
print(mx_curr,mx)
