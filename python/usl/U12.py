import math
a = int(input('Введите трёхзначное число:'))
b = a//100
c = a // 10 % 10
d = a%10
print(str(b)+'+'+str(c)+'+'+str(d)+'='+str(b+c+d))
print((str(b)+'*'+str(c)+'*'+str(d)+'='+str(b*c*d)))
