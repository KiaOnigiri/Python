f=open('24-1.txt')
s=f.read()
d=''
b=[]
for x in s:
    if x.isdigit()==True:
        d+=x
    elif d!='':
        b.append(d)
        d=''
if d!='':
        b.append(d)
print(b)
print(max([int(x) for x in b if '1' not in x and '3' not in x and '5' not in x and '7' not in x and '9' not in x]))
