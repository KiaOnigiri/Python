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
r=[int(x) for x in b]
print(max([int(z) for z in b if 1 not in r and 3 not in r and 5 not in r and 7 not in r and 9 not in r]))
