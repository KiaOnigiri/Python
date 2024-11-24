
def Algoritm(x,y):
    if x<2:
        return 0
    if x==2 and y==1:
        return 1
    if x<16 and y==0:
        return 0
    if x==16:
        y=1
    if x>2:
        return Algoritm(x-2,y)+Algoritm(x//2,y)


print(Algoritm(38,0))
#-2
#//2
