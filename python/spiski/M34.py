def sum3(b):
    for i in range(len(b)):
        for i1 in range(i+1,len(b)):
            for i2 in range(i1+1,len(b)):
                if b[i]+b[i1]==b[i2]:
                    print('{}+{}={}'.format(b[i],b[i1],b[i2]))
                    



from random import *
n=10
b=[randint(1,50) for i in range(n)]
print(b)
sum3(b)
b.sort()
print(b)
sum3(b)
