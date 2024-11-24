import pickle
import hashlib
from random import randint,choice
import os
def myhash(text):
    return hashlib.sha256(text.encode()).hexdigest()
class Game():
    def __init__(self,psw,coins=0,inv={'Броня':{'Стандартное':[],'Обычное':[],'Редкое':[],'Эпическое':[],'Легендарное':[],'Уникальное':[]},'Оружие':{'Стандартное':['Рука'],'Обычное':[],'Редкое':[],'Эпическое':[],'Легендарное':[],'Уникальное':[]}}):
        self.__psw=myhash(psw)
        self.coins=coins
        self.inv=inv
    def get_psw(self):
        return self.__psw
    def add_weap(self,drp):
        self.inv['Оружие'][drp[0]].append(drp[1])
        #self.inv['Оружие']=self.inv['Оружие']
    def check_weap(self,drp):
        if drp[1] in self.inv['Оружие'][drp[0]]:
            return False
        else:
            return True
    def see_weap(self,redkost):
        if redkost=='1' and self.inv['Оружие']['Стандартное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Оружие']['Стандартное'][skidish]}" for skidish in range(len(self.inv['Оружие']['Стандартное']))])
        if redkost=='1' and self.inv['Оружие']['Стандартное']==[]:
            return '*У вас нет стандартного оружия*'
        if redkost=='2' and self.inv['Оружие']['Обычное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Оружие']['Обычное'][skidish]}" for skidish in range(len(self.inv['Оружие']['Обычное']))])
        if redkost=='2' and self.inv['Оружие']['Обычное']==[]:
            return '*У вас нет обычного оружия*'
        if redkost=='3' and self.inv['Оружие']['Редкое']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Оружие']['Редкое'][skidish]}" for skidish in range(len(self.inv['Оружие']['Редкое']))])
        if redkost=='3' and self.inv['Оружие']['Редкое']==[]:
            return '*У вас нет редкого оружия*'
        if redkost=='4' and self.inv['Оружие']['Эпическое']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Оружие']['Эпическое'][skidish]}" for skidish in range(len(self.inv['Оружие']['Эпическое']))])
        if redkost=='4' and self.inv['Оружие']['Эпическое']==[]:
            return '*У вас нет эпического оружия*'
        if redkost=='5' and self.inv['Оружие']['Легендарное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Оружие']['Легендарное'][skidish]}" for skidish in range(len(self.inv['Оружие']['Легендарное']))])
        if redkost=='5' and self.inv['Оружие']['Легендарное']==[]:
            return '*У вас нет легендарного оружия*'
        if redkost=='6' and self.inv['Оружие']['Уникальное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Оружие']['Уникальное'][skidish]}" for skidish in range(len(self.inv['Оружие']['Уникальное']))])
        if redkost=='6' and self.inv['Оружие']['Уникальное']==[]:
            return '*У вас нет уникального оружия*'
    def see_armor(self,redkost):
        if redkost=='0':
            return self.inv['Броня']
        if redkost=='1' and self.inv['Броня']['Стандартное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Броня']['Стандартное'][skidish]}" for skidish in range(len(self.inv['Броня']['Стандартное']))])
        if redkost=='1' and self.inv['Броня']['Стандартное']==[]:
            return '*У вас нет стандартной брони*'
        if redkost=='2' and self.inv['Броня']['Обычное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Броня']['Обычное'][skidish]}" for skidish in range(len(self.inv['Броня']['Обычное']))])
        if redkost=='2' and self.inv['Броня']['Обычное']==[]:
            return '*У вас нет обычной брони*'
        if redkost=='3' and self.inv['Броня']['Редкое']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Броня']['Редкое'][skidish]}" for skidish in range(len(self.inv['Броня']['Редкое']))])
        if redkost=='3' and self.inv['Броня']['Редкое']==[]:
            return '*У вас нет редкой брони*'
        if redkost=='4' and self.inv['Броня']['Эпическое']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Броня']['Эпическое'][skidish]}" for skidish in range(len(self.inv['Броня']['Эпическое']))])
        if redkost=='4' and self.inv['Броня']['Эпическое']==[]:
            return '*У вас нет эпической брони*'
        if redkost=='5' and self.inv['Броня']['Легендарное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Броня']['Легендарное'][skidish]}" for skidish in range(len(self.inv['Броня']['Легендарное']))])
        if redkost=='5' and self.inv['Броня']['Легендарное']==[]:
            return '*У вас нет легендарной брони*'
        if redkost=='6' and self.inv['Броня']['Уникальное']!=[]:
            return '\n'.join([f"{skidish+1}) {self.inv['Броня']['Уникальное'][skidish]}" for skidish in range(len(self.inv['Броня']['Уникальное']))])
        if redkost=='6' and self.inv['Броня']['Уникальное']==[]:
            return '*У вас нет уникальной брони*'
    def change_coins(self, value):
        self.coins=self.coins+value
    def get_coins(self):
        #self.coins=self.coins-1
        return self.coins
    @staticmethod
    def createacc(name,number):
        global Base
        global logged_acc
        if Base.get(name)==None:
            Base[name]=Game(number)
            logged_acc=name
            print(f'Вы успешно создали и вошли в аккаунт с именем "{name}"')
        else:
            print('Ошибка: Аккаунт с таким именем уже существует')
    @staticmethod
    def login(name,number):
        global Base
        global logged_acc
        if Base.get(name)!=None and Base[name].get_psw()==myhash(number):
            logged_acc=name
            print('Вы успешно вошли в аккаунт')
        else:
            print('Ошибка: Неверное имя аккаунта или пароль')
   
class Weapon:
    def __init__(self, damage=1, cost=1, crit_chance=0, rarity='стандартное', status=None, energy_recharge=2, start_energy=10, special=None, name = 'Оружие'):
        self.damage = damage
        self.cost = cost
        self.crit_chance = crit_chance
        self.rarity = rarity
        self.status = status
        self.energy_recharge = energy_recharge
        self.start_energy = start_energy
        self.special = special
        self.name = name

'''
    def total_damage(self):
        raritymultiply = {'common' : 1, 'rare' : 2, 'epic' : 3, 'legendary' : 4}
        if randint(1, 100) <= int(self.crit_chance*100) == True:
            return self.damage * raritymultiply[self.rarity] * self.attack_speed * 2
        else:
            return self.damage * raritymultiply[self.rarity] * self.attack_speed'''


def DropGun():
    rarity = {'Стандартное':0.718, 'Обычное' : 0.180 , 'Редкое' : 0.069 , 'Эпическое' : 0.026, 'Легендарное' : 0.006, 'Уникальное' : 0.001}
    prev = 0
    dropped_chance = randint(1, 1000)
    final_drop=None
    for saved_chance in rarity:
        #print(prev, rarity[saved_chance]*1000+prev)
        if dropped_chance in range(int(prev),int(rarity[saved_chance]*1000)+int(prev)):
            #print(saved_chance)
            final_drop = saved_chance
            break
        else:
            prev += rarity[saved_chance]*1000
    if final_drop=='Стандартное':
        weap=choice(['Плохой револьвер', 'Старый лук', 'Сломанные нунчаки', 'Парные клинки с одним клинком', 'Некачественный палаш', 'Ржавый меч', 'Поломанный клинок', 'Грязный кинжал'])
        print(f'Вы выбили {final_drop.lower()} оружие (71,8%) под названием "{weap}"!')
        return [final_drop,weap]
    if final_drop=='Обычное':
        weap=choice(['Револьвер', 'Лук', 'Нунчаки', 'Парные клинки', 'Палаш', 'Меч', 'Клинок', 'Кинжал'])
        print(f'Вы выбили {final_drop.lower()} оружие (18%) под названием "{weap}"!')
        return [final_drop,weap]
    if final_drop=='Редкое':
        weap=choice(['Качественный револьвер', 'Крепкий лук', 'Хорошие нунчаки', 'Неплохие парные клинки', 'Прочный палаш', 'Сильный меч', 'Ловкий клинок', 'Лёгкий кинжал'])
        print(f'Вы выбили {final_drop.lower()} оружие (6,9%) под названием "{weap}"!')
        return [final_drop,weap]
    if final_drop=='Эпическое':
        weap=choice(['Револьвер ковбоя', 'Мегалук', 'Нунчаки ниндзя', 'Парные клинки возмездия', 'Пронзающий палаш', 'Меч рыцаря', 'Суперловкий клинок', 'Кинжал убийцы'])
        print(f'Вы выбили {final_drop.lower()} оружие (2,6%) под названием "{weap}"!')
        return [final_drop,weap]
    if final_drop=='Легендарное':
        weap=choice(['Лазерный револьвер', 'Электролук', 'Световые нунчаки', 'Огненные парные клинки', 'Всепронзающий  гигантский палаш', 'Лунный меч', 'Тёмный клинок', 'Ядовитый кинжал смерти'])
        print(f'Вы выбили {final_drop.lower()} оружие (0,6%) под названием "{weap}"!')
        return [final_drop,weap]
    if final_drop=='Уникальное':
        weap=choice(['Револьвер "Уничтожитель планет"', 'Лук "Хранитель времени"', 'Нунчаки "Стиратель горизонтов"', 'Парные клинки "Первооткрыватель вселенной"', 'Палаш "Пронзатель ткани пространства"', 'Меч "Созидатель луны"', 'Клинок "Пожиратель света"', 'Кинжал "Творитель правосудия"'])
        print(f'Вы выбили {final_drop.lower()} оружие (0,1%) под названием "{weap}"!')
        return [final_drop,weap]



acc_menu=True
exit_game=False
logged_acc=None
start_game=False
while exit_game==False:
    if acc_menu==True:
        print('')
        print('=====ВХОД В АККАУНТ=====\n')
        Base={}
        with open('file.pkl', 'rb') as fp:
            Base=pickle.load(fp)
        #print(Base)
        #print(Base['Admin'].get_psw())
        while logged_acc==None:
            print('')
            n=input('Введите 1, если хотите создать новый аккаунт;\nВведите 2, если хотите войти в аккаунт:\n')
            print('')
            os.system('cls')
            if n=='1':
                new_name=input('Введите имя для своего нового аккаунта:\n')
                new_psw1=input('Введите пароль для своего нового аккаунта:\n')
                new_psw2=input('Повторите пароль для своего нового аккаунта:\n')
                if new_psw1!=new_psw2:
                    print('Пароли не совпадают, попробуйте ещё раз')
                    continue
                Game.createacc(new_name,new_psw1)
            elif n=='2':
                old_name=input('Введите имя своего аккаунта:\n')
                old_psw=input('Введите пароль своего аккаунта:\n')
                Game.login(old_name,old_psw)
            else:
                print('Вы ввели невозможное значение, пожалуйста, попробуйте ещё раз')
        #Base={}
        with open('file.pkl','wb') as fp:
            pickle.dump(Base,fp)
    acc_menu=False
    '''
    if start_game==True:


        
    start_game=False
    '''
    if acc_menu==False:
        print('')
        print('=====ГЛАВНОЕ МЕНЮ=====\n')
    action=input('Введите 1, чтобы начать игру;\nВведите 2, если хотите сохраниться и выйти из аккаунта;\nВведите 3, если хотите удалить аккаунт;\nВведите 4, если хотите войти в меню роллов оружия;\nВведите 5, если хотите посмотреть кол-во монет, ваш инвентарь оружия или брони;\nВведите 6, если хотите сохраниться и выйти из игры:\n')
    print('')
    if action=='1':
        start_game=True
        print('')
        print('Приятной игры!')
        print('')
    if action=='2':
        acc_menu=True
        #ccoins=Base[logged_acc].get_coins()
        #print(ccoins)
        with open('file.pkl','wb') as fp:
            pickle.dump(Base,fp)
        logged_acc=None
        print('Вы успешно вышли из аккаунта!')
    if action=='3':
        confirm=input('Введите "ПОДТВЕРЖДАЮ", если вы действительно хотите удалить свой аккаунт:\n')
        if confirm!='ПОДТВЕРЖДАЮ':
            print('')
            print('Вы не ввели "ПОДТВЕРЖДАЮ", возвращение в главное меню')
        else:
            print('')
            print(f'Аккаунт с именем {logged_acc} был успешно удалён!')
            del Base[logged_acc]
            acc_menu=True
            logged_acc=None
            with open('file.pkl','wb') as fp:
                pickle.dump(Base,fp)
    if action=='6':
        print('')
        print('Спасибо за игру! Возвращайтесь снова!\n')
        with open('file.pkl','wb') as fp:
            pickle.dump(Base,fp)
        exit_game=True
    if action=='4':
        roll_menu=True
        print('')
        print('Вы вошли в меню ролла оружия!\n')
        while roll_menu:
            weaction=input('\nВведите 1, если хотите начать роллить (Стоимость 100 монет за 1 ролл);\nВведите 2, если хотите посмотреть ваш инвентарь оружия;\nВведите 3, если хотите выйти из меню роллов оружия:\n')
            print('')
            if weaction=='1':
                Base[logged_acc].change_coins(-100)
                drp=DropGun()
                if Base[logged_acc].check_weap(drp):
                    Base[logged_acc].add_weap(drp)
                else:
                    print('\nУ вас уже есть экземпляр данного оружия, все повторки оружий автоматически уничтожаются...\n')
                print(f'\nВаше текущее кол-во монет:\n{Base[logged_acc].get_coins()}\n')
            if weaction=='2':
                redkost=input('\nВведите 1, если хотите посмотреть ваше стандартное оружие;\nВведите 2, если хотите посмотреть ваше обычное оружие;\nВведите 3, если хотите посмотреть ваше редкое оружие;\nВведите 4, если хотите посмотреть ваше эпическое оружие;\nВведите 5, если хотите посмотреть ваше легендарное оружие;\nВведите 6, если хотите посмотреть ваше уникальное оружие;\nВведите 7, если хотите вернуться назад:\n')
                if redkost not in ['1','2','3','4','5','6','7']:
                    print('\nВы ввели невозможное значение, пожалуйста, попробуйте ещё раз\n')
                if redkost in ['1','2','3','4','5','6']:
                    print(Base[logged_acc].see_weap(redkost))
            if weaction=='3':
                roll_menu=False
            if weaction not in ['1','2','3']:
                print('\nВы ввели невозможное значение, пожалуйста, попробуйте ещё раз\n')
    if action=='5':
        activ=True
        while activ:
            inaction=input('\nВведите 1, если хотите посмотреть ваше количество монет;\nВвежите 2, если хотите посмотреть ваш инвентарь оружия;\nВведите 3, если хотите посмотреть ваш инвентарь брони;\nВведите 4, если хотите выйти из меню просмотра инвентаря оружия, инвентаря брони и монет:\n')
            if inaction=='1':
                print(f'\nВаше текущее кол-во монет:\n{Base[logged_acc].get_coins()}\n')
            if inaction=='2':
                redkost=input('\nВведите 1, если хотите посмотреть ваше стандартное оружие;\nВведите 2, если хотите посмотреть ваше обычное оружие;\nВведите 3, если хотите посмотреть ваше редкое оружие;\nВведите 4, если хотите посмотреть ваше эпическое оружие;\nВведите 5, если хотите посмотреть ваше легендарное оружие;\nВведите 6, если хотите посмотреть ваше уникальное оружие;\nВведите 7, если хотите вернуться назад:\n')
                if redkost not in ['1','2','3','4','5','6','7']:
                    print('\nВы ввели невозможное значение, пожалуйста, попробуйте ещё раз\n')
                if redkost in ['1','2','3','4','5','6']:
                    print(Base[logged_acc].see_weap(redkost))
            if inaction=='3':
                #print(Base[logged_acc].see_armor('0'))
                if Base[logged_acc].see_armor('0')=={'Стандартное':[],'Обычное':[],'Редкое':[],'Эпическое':[],'Легендарное':[],'Уникальное':[]}:
                    print(f'\n*Ваш инвентарь брони пока что пуст*\n')
                else:
                    redkost=input('\nВведите 1, если хотите посмотреть вашу стандартную броню;\nВведите 2, если хотите посмотреть вашу обычную броню;\nВведите 3, если хотите посмотреть вашу редкую броню;\nВведите 4, если хотите посмотреть вашу эпическую броню;\nВведите 5, если хотите посмотреть вашу легендарную броню;\nВведите 6, если хотите посмотреть вашу уникальную броню;\nВведите 7, если хотите вернуться назад:\n')
                    if redkost not in ['1','2','3','4','5','6','7']:
                        print('\nВы ввели невозможное значение, пожалуйста, попробуйте ещё раз\n')
                    if redkost in ['1','2','3','4','5','6']:
                        print(Base[logged_acc].see_armor(redkost))
            if inaction=='4':
                activ=False
            if inaction not in ['1','2','3','4']:
                print('\nВы ввели невозможное значение, пожалуйста, попробуйте ещё раз\n')
    if action not in ['1','2','3','4','5','6']:
        print('\nВы ввели невозможное значение, пожалуйста, попробуйте ещё раз\n')
                
    

