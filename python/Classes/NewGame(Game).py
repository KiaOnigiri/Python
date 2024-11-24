from random import randint,choice
class Game():
    def __init__(self,psw,coins=0,inv={'Броня':[],'Оружие':['Рука']}):
        self.__psw=myhash(psw)
        self.coins=coins
        self.inv=inv
def Drop():
    rarity = {'стандартное':0.718, 'обычное' : 0.180 , 'редкое' : 0.069 , 'эпическое' : 0.026, 'легендарное' : 0.006, 'уникальное' : 0.001}
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
    if final_drop=='стандартное':
        weap=choice(['Плохой револьвер', 'Ржавый лук', 'Сломанные нунчаки', 'Парные клинки с одним клинком', 'Некачественный палаш', 'Потрёпанный меч', 'Поломанный клинок', 'Грязный кинжал'])
        print(f'Вы выбили {saved_chance} оружие (71,8%) под названием "{weap}"!')
        return weap
    if final_drop=='обычное':
        weap=choice(['Револьвер', 'Лук', 'Нунчаки', 'Парные клинки', 'Палаш', 'Меч', 'Клинок', 'Кинжал'])
        print(f'Вы выбили {saved_chance} оружие (18%) под названием "{weap}"!')
        return weap
    if final_drop=='редкое':
        weap=choice(['Качественный револьвер', 'Крепкий лук', 'Хорошие нунчаки', 'Неплохие парные клинки', 'Прочный палаш', 'Сильный меч', 'Ловкий клинок', 'Лёгкий кинжал'])
        print(f'Вы выбили {saved_chance} оружие (6,9%) под названием "{weap}"!')
        return weap
    if final_drop=='эпическое':
        weap=choice(['Револьвер ковбоя', 'Мегалук', 'Нунчаки рыцаря', 'Парные клинки возмездия', 'Пронзающий палаш', 'Супер сильный меч', 'Очень ловкий клинок', 'Периный кинжал'])
        print(f'Вы выбили {saved_chance} оружие (2,6%) под названием "{weap}"!')
        return weap
    if final_drop=='легендарное':
        weap=choice(['Лазерный револьвер', 'Электролук', 'Световые нунчаки', 'Огненные парные клинки', 'Всепронзающий  гигантский палаш', 'Лунный меч', 'Тёмный клинок', 'Ядовитый кинжал смерти'])
        print(f'Вы выбили {saved_chance} оружие (0,6%) под названием "{weap}"!')
        return weap
    if final_drop=='уникальное':
        weap=choice(['Револьвер "Уничтожитель планет"', 'Лук "Хранитель времени"', 'Нунчаки "Стиратель горизонтов"', 'Парные клинки "Первооткрыватель вселенной"', 'Палаш "Пронзатель ткани пространства"', 'Меч "Созидатель луны"', 'Клинок "Пожиратель света"', 'Кинжал "Творитель правосудия"'])
        print(f'Вы выбили {saved_chance} оружие (0,1%) под названием "{weap}"!')
        return weap


   
class Weapon:
    def __init__(self, damage=1, cost=1, crit_chance=0, rarity='standart', status=None, energy_recharge=2, start_energy=10, special=None, name = 'Оружие'):
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
        
# --------------------------------------------------------------------------------------
start_game=True
while start_game:
    action=input('Введите 1, чтобы начать игру;\n 3 чтобы пака;\n 2 гачамуча:\n')
    if action=='3':
        print('Пока')
        start_game=False
        continue
    if action=='2':
        print(Drop())
    
