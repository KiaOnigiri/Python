import pickle
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
mxres=Max(0)
with open("mxrslt.pkl", "wb") as fp:
    pickle.dump(mxres, fp)
