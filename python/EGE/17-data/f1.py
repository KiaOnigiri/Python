#содержимое файла как строку вывести на экран
f = open("24-1.txt",'r')
s = f.read()
f.close()
#print(s)
x=''
mx=-1
for c in s:
    if c.isdigit():
        x += c
        if int(x)>mx:
            mx=int(x)        
    else:    
        x=''
print(mx)