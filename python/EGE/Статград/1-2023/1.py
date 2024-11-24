x,y,a,b=input().split()
x,y,a,b=int(x),int(y),int(a),int(b)
k=0
while True:
    y+=a
    k+=1
    if y>=x:
        break
    x+=b
    k+=1
print(k)
