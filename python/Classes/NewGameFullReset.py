import pickle
import hashlib
def myhash(text):
    return hashlib.sha256(text.encode()).hexdigest()
class Game():
    def __init__(self,psw,coins=0,inv={'Броня':{'Стандартное':[],'Обычное':[],'Редкое':[],'Эпическое':[],'Легендарное':[],'Уникальное':[]},'Оружие':{'Стандартное':['Рука'],'Обычное':[],'Редкое':[],'Эпическое':[],'Легендарное':[],'Уникальное':[]}}):
        self.__psw=myhash(psw)
        self.coins=coins
        self.inv=inv
    def get_psw(self):
        return self.__psw
    def see_inv(self):
        return self.inv['Оружие'].values()
Base={}
Base['Admin']=Game('Admin12345',9999999999)
#print(Base['Admin'].see_inv())
#print(Base['Admin'].get_psw())
with open('file.pkl','wb') as fp:
    pickle.dump(Base,fp)
print('*All accounts has been successfully restored*')
