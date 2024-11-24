f=open('24-181.txt')
s=f.read()
k=0
for i in range(len(s)-12):
    if s[i+1]=='7' and s[i].isalpha() and s[i+2].isalpha()==False and s[i+3].isalpha()==False and s[i+4].isalpha()==False
        k+=1
print(k)
