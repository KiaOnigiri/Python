from tkinter import *
from tkinter.ttk import Combobox
import random
def clicked():
    k.append(0)
    cc.configure(text=str(len(k)))
    btn.place(x=random.randint(20,400),y=random.randint(20,200))
'2,3,6,8,10,16'
'''  
  
def inAny(x,y):
    b=[]
    while x>0:
        ost=x%y
        if ost>9:
            ost=chr(ord('A')+ost-10)
        b.append(ost)
        x//=y
    b.reverse()
    return b
def fromAny(x,y):
    b=[]
    for j in x:
        if j in ['0','1','2','3','4','5','6','7','8','9']:
            b.append(int(j))
        else:
            k=ord('A')+ord(j)-120
            if k>=y:
                return False
            b.append(k)
    b.reverse()
    a=0
    for i in range(0,len(b)):
        a+=b[i]*(y**i)
    return a
def clicked():
    c=chislo.get()
    i=izkakoy.get()
    v=vkakuyu.get()
    if v=='1' or v=='0':
        res='Ошибка'
        gg.configure(text=res)
    else:
        res = inAny(fromAny(str(c),int(i)),int(v))
        if res==[]:
            res='Ошибка'
            gg.configure(text=res)
        gg.configure(text=res)
  

window = Tk()  
window.title("Перевод систем счисления")  
window.geometry('450x207')  
lbl = Label(window, text="Переводимое число:", font=("Arial Bold", 14))  
lbl.grid(column=0, row=0)
lbl = Label(window, text="Из какой системы счисления:", font=("Arial Bold", 14))  
lbl.grid(column=0, row=1)
lbl = Label(window, text="В какую систему счисления:", font=("Arial Bold", 14))  
lbl.grid(column=0, row=2)
lbl = Label(window, text="Цифры, которые больше 9, вводить английскими заглавными буквами", font=("Arial Bold", 8), fg="grey")  
lbl.grid(column=0, row=8)
lbl = Label(window, text="К примеру, чтобы записать цифру 10, используйте английскую букву A", font=("Arial Bold", 8), fg="grey")  
lbl.grid(column=0, row=9)
lbl = Label(window, text=" ", font=("Arial Bold", 10))  
lbl.grid(column=0, row=3)
lbl = Label(window, text="Вывод:", font=("Arial Bold", 14))  
lbl.grid(column=0, row=7)
gg = Label(window, text="-", font=("Arial Bold", 10))  
gg.grid(column=1, row=7)
chislo = Entry(window,width=9)  
chislo.grid(column=1, row=0)
izkakoy = Entry(window,width=4)  
izkakoy.grid(column=1, row=1)
vkakuyu = Entry(window,width=4)  
vkakuyu.grid(column=1, row=2)  
btn = Button(window, text="Пуск", command=clicked)  
btn.grid(column=1, row=4)
window.mainloop()
'''
k=[]
window = Tk()  
window.title("Кликер")  
window.geometry('450x207')
lbl = Label(window, text="Поинты", font=("Arial Bold", 14))  
lbl.grid(column=0, row=0)
cc = Label(window, text="0", font=("Arial Bold", 14))  
cc.grid(column=1, row=0)
btn = Button(window, text="Клик!", command=clicked)  
btn.grid(column=7, row=0)
btn.place(x=random.randint(20,400),y=random.randint(20,200))
window.mainloop()
