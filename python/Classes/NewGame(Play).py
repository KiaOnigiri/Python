import time
from random import randint,choice
class Weapon:
    def __init__(self, damage1skill=1, damage2skill=1, cost1skill=1, cost2skill=1, crit_chance=0, rarity='стандартное', status=None, energy_recharge1skill=2, energy_recharge2skill=2, start_energy=10, rad1skill=None, rad2skill=None, special=None, name = 'Оружие'):
        self.damage1skill = damage1skill
        self.damage2skill = damage2skill
        self.cost1skill = cost1skill
        self.cost2skill = cost2skill
        self.rad1skill = rad1skill
        self.rad2skill = rad2skill
        self.energy_recharge1skill = energy_recharge1skill
        self.energy_recharge2skill = energy_recharge2skill
        self.crit_chance = crit_chance
        self.rarity = rarity
        self.status = status
        self.start_energy = start_energy
        self.special = special
        self.name = name
        
start_game=True
fld=[['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
rndnt=randint(0,3)
if rndnt==0:
    x,y=0,0
    x1,y1=9,9
if rndnt==1:
    x,y=9,0
    x1,y1=0,9
if rndnt==2:
    x1,y1=9,0
    x,y=0,9
if rndnt==3:
    x1,y1=0,0
    x,y=9,9
last_pressed=None
enemy_count=3
enemy_r=2
while start_game:
    if last_pressed=='s':
        for i in range(-1,1+1):
            for j in range(1,2+1):
                if 0<=y+j<=9 and 0<=x+i<=9:
                    fld[y+j][x+i]='#'
    if last_pressed=='w':
        for i in range(-1,1+1):
            for j in range(-2,-1+1):
                if 0<=y+j<=9 and 0<=x+i<=9:
                    fld[y+j][x+i]='#'
    if last_pressed=='d':
        for j in range(-1,1+1):
            for i in range(1,2+1):
                if 0<=y+j<=9 and 0<=x+i<=9:
                    fld[y+j][x+i]='#'
    if last_pressed=='a':
        for j in range(-1,1+1):
            for i in range(-2,-1+1):
                if 0<=y+j<=9 and 0<=x+i<=9:
                    fld[y+j][x+i]='#'
    fld[y][x]='p'
    if fld[y1][x1]=='#':
        fld[y1][x1]='E'
    else:
        fld[y1][x1]='e'
    for i in range(-enemy_r,enemy_r+1):
        for j in range(-enemy_r,enemy_r+1):
            if 0<=y1+j<=9 and 0<=x1+i<=9 and fld[y1+j][x1+i]=='*':
                fld[y1+j][x1+i]='x'
            elif 0<=y1+j<=9 and 0<=x1+i<=9 and fld[y1+j][x1+i]=='#':
                #print(fld[y1+j][x1+i],y1+j,x1+i,'\n'.join([' '.join(z) for z in fld]))
                fld[y1+j][x1+i]='@'
            elif 0<=y1+j<=9 and 0<=x1+i<=9 and fld[y1+j][x1+i]=='p':
                fld[y1+j][x1+i]='P'
    print('===================')
    print('       Field       ')
    print('\n'.join([' '.join(z) for z in fld]))
    print('   Energy: 10/10   ')
    print('===================')
    pressed=input('Введите w,a,s,d для хода в определённую сторону;\nвведите 1, если хотите завершить ход:\n')
    if pressed=='1':
        print('Ваши ходы завершены, переход хода к врагу...')
        for hod in range(enemy_count):
            fld=[['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
            
            time.sleep(1)
            if last_pressed=='s':
                for i in range(-1,1+1):
                    for j in range(1,2+1):
                        if 0<=y+j<=9 and 0<=x+i<=9:
                            fld[y+j][x+i]='#'
            if last_pressed=='w':
                for i in range(-1,1+1):
                    for j in range(-2,-1+1):
                        if 0<=y+j<=9 and 0<=x+i<=9:
                            fld[y+j][x+i]='#'
            if last_pressed=='d':
                for j in range(-1,1+1):
                    for i in range(1,2+1):
                        if 0<=y+j<=9 and 0<=x+i<=9:
                            fld[y+j][x+i]='#'
            if last_pressed=='a':
                for j in range(-1,1+1):
                    for i in range(-2,-1+1):
                        if 0<=y+j<=9 and 0<=x+i<=9:
                            fld[y+j][x+i]='#'
            fld[y][x]='p'
            if x-x1>enemy_r and abs(x-x1)>abs(y-y1):
                x1+=1
            elif y-y1>enemy_r and abs(y-y1)>abs(x-x1):
                y1+=1
            elif x1-x>enemy_r and abs(x-x1)>abs(y-y1):
                x1-=1
            elif y1-y>enemy_r and abs(y-y1)>abs(x-x1):
                y1-=1
            elif x-x1>enemy_r and y-y1>enemy_r and abs(x-x1)==abs(y-y1):
                chc=randint(0,1)
                if chc==0:
                    x1+=1
                if chc==1:
                    y1+=1
                #choice(x1+=1,y1+=1)
            elif x-x1>enemy_r and y1-y>enemy_r and abs(x-x1)==abs(y-y1):
                chc=randint(0,1)
                if chc==0:
                    x1+=1
                if chc==1:
                    y1-=1
                #choice(x1+=1,y1-=1)
            elif x1-x>enemy_r and y-y1>enemy_r and abs(x-x1)==abs(y-y1):
                chc=randint(0,1)
                if chc==0:
                    x1-=1
                if chc==1:
                    y1+=1
                #choice(x1-=1,y1+=1)
            elif x1-x>enemy_r and y1-y>enemy_r and abs(x-x1)==abs(y-y1):
                chc=randint(0,1)
                if chc==0:
                    x1-=1
                if chc==1:
                    y1-=1
                #choice(x1-=1,y1-=1)
            if fld[y1][x1]=='#':
                fld[y1][x1]='E'
            else:
                fld[y1][x1]='e'
            for i in range(-enemy_r,enemy_r+1):
                for j in range(-enemy_r,enemy_r+1):
                    if 0<=y1+j<=9 and 0<=x1+i<=9 and fld[y1+j][x1+i]=='*':
                        fld[y1+j][x1+i]='x'
                    elif 0<=y1+j<=9 and 0<=x1+i<=9 and fld[y1+j][x1+i]=='#':
                        #print(fld[y1+j][x1+i],y1+j,x1+i,'\n'.join([' '.join(z) for z in fld]))
                        fld[y1+j][x1+i]='@'
                    elif 0<=y1+j<=9 and 0<=x1+i<=9 and fld[y1+j][x1+i]=='p':
                        fld[y1+j][x1+i]='P'
            if hod!=enemy_count-1:
                print('===================')
                print('       Field       ')
                print('\n'.join([' '.join(z) for z in fld]))
                print('   Energy: 10/10   ')
                print('===================')
            #print(abs(x-x1),abs(y-y1),x1,y1,x,y)
    if y<9 and pressed=='s' and (fld[y+1][x]!='e'):
        y+=1
        last_pressed='s'
    if y>0 and pressed=='w' and (fld[y-1][x]!='e'):
        y-=1
        last_pressed='w'
    if x<9 and pressed=='d' and (fld[y][x+1]!='e'):
        x+=1
        last_pressed='d'
    if x>0 and pressed=='a' and (fld[y][x-1]!='e'):
        x-=1
        last_pressed='a'
    if pressed not in ['1','w','a','s','d']:
        print('\nВы ввели невозможное значение, пожалуйста, попробуйте ещё раз\n')
    fld=[['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

    
    
