import pickle
from random import *
import time
class Max:
    def __init__(self,mxx):
        self.mxx=mxx
    def mx(self,mx):
        return max(mx,self.mxx)
    def __getstate__(self) -> dict:
        state = {}
        state["mxx"]=self.mxx
        return state
    def __setstate__(self, state: dict):
        self.mxx=state["mxx"]
'''
mxres=Max(0)
with open("mxrslt.pkl", "wb") as fp:
    pickle.dump(mxres, fp)'''
with open("mxrslt.pkl", "rb") as fp:
    mxres = pickle.load(fp)
print(f'ВАШ ТЕКУЩИЙ МАКСИМАЛЬНЫЙ WinStreak: {mxres.mx(0)}')
time.sleep(1.5)
n=int(input('ВВЕДИТЕ "123", ЧТОБЫ НАЧАТЬ ИГРУ "Камень-Ножницы-Бумага": '))
if n==123:
    print('')
    print('')
    time.sleep(1)
    print('ИГРА НАЧАЛАСЬ...')
    time.sleep(1)
    print('')
    print('')
    #Win=True
    k=0
    flag=False
    flag1=False
    flag2=False
    while True:
        time.sleep(1)
        if flag2:
            print('')
            print('ПОВТОР...')
            print('')
            flag2=False
            time.sleep(1)
        elif flag1:
            print('')
            print('')
            print('')
            print('СЛЕДУЮЩАЯ ИГРА...')
            print('')
            time.sleep(1)
        elif flag:
            print('')
            print('СЛЕДУЮЩИЙ РАУНД...')
            print('')
            time.sleep(1)
        print('ВВЕДИТЕ "1", ЧТОБЫ ВЫБРАТЬ КАМЕНЬ, ВВЕДИТЕ "2", ЧТОБЫ ВЫБРАТЬ НОЖНИЦЫ, ВВЕДИТЕ "3", ЧТОБЫ ВЫБРАТЬ БУМАГУ')
        m=int(input(': '))
        if m!=1 and m!=2 and m!=3:
            print('ОШИБОЧКА, ВЫ НЕ МОЖЕТЕ ЭТО ВВЕСТИ! ДАВАЙТЕ ПОПРОБУЕМ ЕЩЁ РАЗ')
            flag2=True
            continue
        print('')
        print('ВАШ СОПЕРНИК ВЫБИРАЕТ...')
        print('')
        time.sleep(randint(1,3))
        h=randint(1,3)
        if h==1:
            p='КАМЕНЬ'
        if h==2:
            p='НОЖНИЦЫ'
        if h==3:
            p='БУМАГУ'
        print(f'ВАШ СОПЕРНИК ВЫБРАЛ {p}...')
        print('')
        time.sleep(1.5)
        if (m==1 and h==3) or (m==2 and h==1) or (m==3 and h==2):
            #Win=False
            flag1=True
            print('ВЫ ПРОИГРАЛИ :(')
            time.sleep(0.75)
            print('')
            print(f'ВАШ WinStreak БЫЛ РАВЕН {k}')
            time.sleep(0.75)
            print('')
            print(f'ВАШ НЫНЕШНИЙ МАКСИМАЛЬНЫЙ WinStreak СОСТАВЛЯЕТ {mxres.mx(k)}')
            mxres=Max(mxres.mx(k))
            print('')
            with open("mxrslt.pkl", "wb") as fp:
                pickle.dump(mxres, fp)
        elif (m==1 and h==1) or (m==2 and h==2) or (m==3 and h==3):
            print('Вы СЫГРАЛИ В НИЧЬЮ -.-')
            print('')
            flag1=False
            time.sleep(0.75)
            print(f'ВАШ ТЕКУЩИЙ WinStreak СОСТАВЛЯЕТ {k}')
        else:
            print('ПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ :)')
            print('')
            k+=1
            flag=True
            flag1=False
            time.sleep(0.75)
            print(f'ВАШ ТЕКУЩИЙ WinStreak СОСТАВЛЯЕТ {k}')
else:
    time.sleep(1)
    print('ВЫ НЕ ВВЕЛИ "123", ИГРА НЕ БЫЛА НАЧАТА...')
        


