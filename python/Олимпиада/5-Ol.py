n=int(input())
x,y=0,0
for i in range(n):
    s16=input()
    if len(s16)==2:
        sm=int(s16[0],16)+int(s16[1],16)
    else:
        sm=int(s16[0],16)
    p=sm%5
    if p==1:
        y+=1
    elif p==2:
        x+=1
    elif p==3:
        y-=1
    elif p==4:
        x-=1
print(x,y)
