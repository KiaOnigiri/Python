def ege15(x,A):
    F=(x&20777!=0)<=((x&12332==0)<=(x&A!=0))
    F=bool(F)
    return F


for A in range(16641,16641+1):
    flag=True
    for x in range(0,5000000+1):
        if ege15(x,A)==False:
            flag=False
            break
    if flag==True:
        print(A)
        break
#16641
