def dels(x):
    a=[]
    for i in range(1,x+1):
        if x%i==0:
            a.append(i)
    return a


#k=int(input('Введите число: '))
print(dels(60),dels(80))
