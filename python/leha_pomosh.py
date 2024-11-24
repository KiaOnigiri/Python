from random import randint
def Drop(barrier):
    #Барьер = сколько редкостей остаётся
    rarity = {'common':0.500, 'rare' : 0.300 , 'epic' : 0.150 , 'legendary' : 0.050}
    max_colvo=0
    for znach in rarity.items():
        znach=list(znach)
        max_colvo+=znach[1]*1000
        if znach[0]==barrier:
            break
    max_colvo=int(max_colvo)
    prev = 0
    dropped_chance = randint(1, max_colvo)
    final_drop=None
    for saved_chance in rarity:
        if dropped_chance in range(int(prev),int(rarity[saved_chance]*1000)+int(prev)):
            final_drop = saved_chance
            break
        else:
            prev += rarity[saved_chance]*1000
    return final_drop
print(Drop('epic'))
