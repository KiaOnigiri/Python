for i in range(8**3,8**4):
    n=oct(i)[2:]
    r=[int(x) for x in n]
    s1=oct(r[0]+r[1])[2:]
    s2=oct(r[2]+r[3])[2:]
    b=sorted([s1,s2],key=int)
    if b[0]+b[1]=='717':
        print('2')
    if b[0]+b[1]=='1511':
        print('3')
    if b[0]+b[1]=='1214':
        print('4', b[0], b[1])
    
