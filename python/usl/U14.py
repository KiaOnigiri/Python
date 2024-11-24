a = int(input())
if a  %7 == 1:
    print('Суббота')
elif a % 7 ==2:
    print('Пятница')
elif a % 7 ==3:
    print('Четверг')
elif a % 7 ==4:
    print('Среда')
elif a % 7 ==5:
    print('Вторник')
elif a % 7 ==6:
    print('Понедельник')
else:
    print('Воскресенье')
