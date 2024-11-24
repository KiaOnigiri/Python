a=''
for i in range(22):
    x=i
    if i>=10:
        x=chr(ord('a')+i-10)
    a+=str(x)
b=''
for i in range(13):
    x=i
    if i>=10:
        x=chr(ord('a')+i-10)
    b+=str(x)
for x in a:
    for y in b:
        
        res=(int(f'{x}23{x}5',22)-int(f'67{y}9{y}',13))
        if res%57==0:
            print(x,y,res/57)
