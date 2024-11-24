for x in '0123456789ABCDEFG':
    t1='135'+x+'9'
    t2='9'+x+'531'
    if (int(t1,17)+int(t2,17))%9==0:
        print((int(t1,17)+int(t2,17))//9,x)
#101340
