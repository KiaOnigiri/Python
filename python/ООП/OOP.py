class Zhopa:
    "Класс для объяснения как работает ООП"
    color='black'
    size=1
    def set_coords(self,x,y):
        self.x=x
        self.y=y
    def get_coords(self):
        return (self.x,self.y)
print(Zhopa.__doc__)
print(Zhopa.color)
Zhopa.color='white'#сменить данное класса
print(Zhopa.color)
print('--------------')
print(Zhopa.__dict__)#хар-ки класса
print('--------------')
a=Zhopa()
print(type(a))#тип объекта а (в этом случае объект класса)
a.color='green'
print(a.__dict__)
print('--------------')
#все хери с attr применимы не только к классам, но и к объектам классов
#setattr() - устанавливает аттрибут на значение
setattr(Zhopa,'beauty',3)
print(Zhopa.beauty)
print('--------------')
#getattr()- пробует взять аттрибут из класса
print(getattr(Zhopa, 'color', False))
print(getattr(Zhopa, 'strength', False))
#del Zhopa.color - удалит аттрибут цвета из жопы
#delattr(Zhopa,'color')- тоже самое что в предыдущей строке
#hasattr(Zhopa,'burnable') - возвращает Тру или Фолз (есть или нет в классе такой аттрибут)
print('--------------')
a.set_coords(26,52)
print(a.get_coords())
