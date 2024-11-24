g=input('Choose your option - ')
if g=='Calc':
    #подсчёт сколько надо написать скобочек для меня
    n=int(input('Кол-во строчек: '))
    n1=int(n*49/40)
    n2=(n*49)%40
    print('{} строчек и ещё {} скобочек'.format(n1,n2))
if g=='CalcForLove':
    #подсчёт сколько надо написать скобочек для Вари
    n=int(input('Кол-во строчек: '))
    n1=int(n*50/41)
    n2=(n*50)%41
    print('{} строчек и ещё {} скобочек'.format(n1,n2))
if g=='Count':
    #проверка правильно ли я написал
    h=len(list(input('Копируй все скобочки сюда: ')))/49
    print(h)
    if float(int(h))==h:
        print('Правильно')
    else:
        print('Неправильно')
if g=='CountForLove':
    #проверка правильно ли Варя написала
    h=len(list(input('Копируй все скобочки сюда: ')))/50
    print(h)
    if float(int(h))==h:
        print('Правильно')
    else:
        print('Неправильно')
    
