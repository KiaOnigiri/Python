b=['']+[str(smth) for smth in range(0,1000)]
d=[]
for x in '0123456789':
    for y in '0123456789':
        for z in b:
            if int(f'54{x}1{y}3{z}7')%18579==0:
                d.append([int(f'54{x}1{y}3{z}7'),int(f'54{x}1{y}3{z}7')/18579])
for x in list(sorted(d)):
    print(*x)
        
            
