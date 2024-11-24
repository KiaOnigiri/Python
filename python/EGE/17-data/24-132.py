f=open("24-J1.txt")
s=f.read()
k='КОТ'
while k in s:
    k+='КОТ'
k=k[:-3]
print(len(k)//3)
