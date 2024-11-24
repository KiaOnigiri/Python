from tkinter import *
import random
def clicked1():
    q.append(0)
    if q[-1]==0:
        btn1.configure(text='Клик!')
        k1=[]
    k.append(1)
    k1.append(1)
    k2.append(-1)
    cc.configure(text=str(sum(k)))
    btn1.place(x=random.randint(20,400),y=random.randint(20,190))
    #btn.configure(height = random.randint(0,1), width = random.randint(0,2))
    if sum(k2)==-20:
        btn2.configure(text='Кликнии(')
    if sum(k2)==-50:
        btn2.configure(text='Я ОБИДЕЛАСЬ')
    #(sum(k2),sum(k1), 'я грустный')
    
def clicked2():
    q.append(1)
    if q[-1]==1:
        btn2.configure(text='Клик!')
        k2=[]
    k.append(1)
    k1.append(-1)
    k2.append(1)
    cc.configure(text=str(sum(k)))
    btn2.place(x=random.randint(20,400),y=random.randint(20,190))
    #btn.configure(height = random.randint(0,1), width = random.randint(0,2))
    if sum(k1)==-20:
        btn1.configure(text='КЛИКАЙ')
    if sum(k1)==-50:
        btn1.configure(text='ЧТОБ ТЕБЯ')
    #(sum(k2),sum(k1),'я злой')
    
q=[-2]
k=[]
k1=[]
k2=[]
window = Tk()  
window.title("Кликер")  
window.geometry('450x207')
window.config(bg = '#E6FEDE')
lbl = Label(window, text="Поинты:", font=("Arial Bold", 14),bg = '#E6FEDE')  
lbl.grid(column=0, row=0)
cc = Label(window, text="0", font=("Arial Bold", 14),bg = '#E6FEDE')  
cc.grid(column=1, row=0)
btn1 = Button(window, text="Клик!", command=clicked1, bg='black', fg="white")  
btn1.grid(column=7, row=0)
btn1.place(x=random.randint(20,400),y=random.randint(20,190))
btn2 = Button(window, text="Клик!", command=clicked2, bg='white', fg="black")  
btn2.grid(column=7, row=0)
btn2.place(x=random.randint(20,400),y=random.randint(20,190))
window.mainloop()
