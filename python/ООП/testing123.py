class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
    
    def set_old(self, old):
        self.__old = old

    old = property(lambda self : self.__old, lambda self,old: old)


p = Person('Сергей', 20)
p.old = 23
print(p.old)
#old=property(lambda self:self.__old,lambda self,old: self.__old=old)
