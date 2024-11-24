a = int(input('A='))
b = int(input('B='))
c = 180-a-b
if a == 90 or b == 90 or c == 90:
    print('Прямоугольный')
elif a < 90 and b < 90 and c < 90:
    print('Остроугольный')
else:
    print('Тупоугольный')
