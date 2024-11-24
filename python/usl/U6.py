A = int(input('Длина 1 - '))
B = int(input('Ширина 1 - '))
C = int(input('Длина 2 - '))
D = int(input('Ширина 2 - '))
if A*B > C*D:
    print('Первый прямоугольник больще первого на ' + str(abs(A*B-C*D)))
elif C*D > A*B:
    print('Второй прямоугольник больще первого на ' + str(abs(C*D-A*B)))
else:
    print('Прямоугольники равны')
