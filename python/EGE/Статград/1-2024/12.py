c='0'+100*'3'+'2'*1000+'23'*333+'0'
#c='022330'
k=0
while '00' not in c:
    k+=1
    c=c.replace('033','1302')
    c=c.replace('03','120')
    c=c.replace('023','203')
    c=c.replace('02','20')
print(c.count('1'),c.count('2'),c.count('3'))
    
