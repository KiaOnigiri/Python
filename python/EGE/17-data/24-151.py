f=open('24-j9.txt')
s=f.read()
g=0
for i in range(2,len(s)-2):
    if s[i-2]==s[i+2] and s[i-1]==s[i+1]:
        g+=1
print(g)
    
            
