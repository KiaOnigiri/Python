from random import randint, choice
class Drop:
    def __init__(self):
        self.rarity = {'common' : 0.5 , 'rare' : 0.3 , 'epic' : 0.15, 'legendary' : 0.05}
        self.type = []

    def chooserarity(self):
        prev = 0
        dropped_chance = randint(1, 100)
        for saved_chance in self.rarity:
            print(prev,self.rarity[saved_chance]*100+prev)
            if dropped_chance in range(int(prev),int(self.rarity[saved_chance]*100)+int(prev)):                
                return saved_chance
            else:
                prev += self.rarity[saved_chance]*100
            


    def return_drop(self):
        return f'Вы выбили {self.chooserarity()} {choice(self.type)}!'

    
    
class Melee(Drop):
    def __init__(self):
        super().__init__()
        self.type = ['sword', 'two_armed_sword', 'dagger']

ml = Melee()
print(ml.return_drop())
