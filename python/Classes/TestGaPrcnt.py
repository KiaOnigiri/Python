import random
import pickle
class GayLvl:
    def __init__(self,name,idk):
        self.name=name
        self.idk=idk
    #def measureGayPrcnt(self):
    #    x=random.randint(1,100)
    #    return "%s's gay percent is %s" % (self.name, x)

    def update(self):
        y[0]+=1
        y[1]+='a'
        print('{}, {}'.format(y[1],y[0]))
    def unupdate(self):
        y[0]-=1
        y[1]=y[1][:-1]
        print('{}, {}'.format(y[1],y[0]))
    #n=input()
    #if n=='1':
    def __getstate__(self) -> dict:  # Как мы будем "сохранять" класс
        state = {}
        state["name"]=y[1]
        state["idk"]=y[0]
        return state
    #if n=='2':
        #def __getstate__(self) -> dict:  # Как мы будем "сохранять" класс
            #state = {}
            #state["name"]=y[1][:-1]
            #state["idk"]=y[0]-1
            #return state
    def __setstate__(self, state: dict):  # Как мы будем восстанавливать класс из байтов
        self.name=state["name"]
        self.idk=state["idk"]
        y.append(self.idk)
        y.append(self.name)
    def __repr__(self):
        return f"{self.__class__}: {self.name}, {self.idk}"
    def __str__(self):
        return f"{self.name}, {self.idk}"
y=[]
Leha=GayLvl("Leha",5)
n=input()

with open("file.pkl", "rb") as fp:
    gl = pickle.load(fp)
deserialized = pickle.dumps(gl)
b = pickle.loads(deserialized)
if n=='1':
    Leha.update()
if n=='2':
    Leha.unupdate()


#print(Kolya.measureGayPrcnt())
#print(Leha.measureGayPrcnt())
#with open("file.pkl", "wb") as fp:
#    pickle.dump(Kolya,fp)
#    print('Yeee')
with open("file.pkl", "wb") as fp:
    pickle.dump(Leha, fp)
'''
class Materials:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def fly(self):
        return "Omg, it flies"
class TheWorld(Materials):
    def brake(self):
        return "How did you do that???"
yooo=TheWorld("Earth","Rainbow")
print(yooo.brake())
'''
