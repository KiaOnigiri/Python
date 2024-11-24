b=['11010','1100','010','01100','0111','111','101','00','100']
h=len(max(b,key=len))
a=[]
for i in range(2**h):
    bini=bin(i)[2:]
    x='0'*(h-len(bini))+bini
    g=0
    for y in b:
        if x[:len(y)]==y or (x in y):
            g=1
            break
    if g==0:
        a.append(x)
print(sorted(a, key=len))
