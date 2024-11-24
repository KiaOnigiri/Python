import pickle
class Sohr:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def __getstate__(self) -> dict:
        state = {}
        state["name"]='Leha'
        state["number"]=5
        return state
World=Sohr("Leha",5)
with open("file.pkl", "wb") as fp:
    pickle.dump(World, fp)
print('*The data has been returned to initial state*')
