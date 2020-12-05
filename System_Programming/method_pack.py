from tkinter import *

root = Tk()
f_top = Frame(root)
lb = Label(width=15)
e1 = Entry(text='Код цвета', width=20)
e1.insert(0, 'Код цвета')
lb['text'] = 'Цвет'

def ins():
    e1.delete(0, END)
    e1.insert(0, "#ff0000")
    lb['text'] = 'Красный'
def ins2():
    e1.delete(0, END)
    e1.insert(0, "#FFA500")
    lb['text'] = 'Оранжевый'
def ins3():
    e1.delete(0, END)
    e1.insert(0, "#FFFF00")
    lb['text'] = 'Жёлтый'
def ins4():
    e1.delete(0, END)
    e1.insert(0, "#00FF00")
    lb['text'] = 'Зелёный'
def ins5():
    e1.delete(0, END)
    e1.insert(0, "#00FFFF")
    lb['text'] = 'Голубой'
def ins6():
    e1.delete(0, END)
    e1.insert(0, "#0000FF")
    lb['text'] = 'Синий'
def ins7():
    e1.delete(0, END)
    e1.insert(0, "#800080")
    lb['text'] = 'Фиолетовый'


but = Button(bg='#ff0000', command=ins, width=4)
but2 = Button(bg='#FFA500', command=ins2, width=4)
but3 = Button(bg='#FFFF00', command=ins3, width=4)
but4 = Button(bg='#00FF00', command=ins4, width=4)
but5 = Button(bg='#00FFFF', command=ins5, width=4)
but6 = Button(bg='#0000FF', command=ins6, width=4)
but7 = Button(bg='#800080', command=ins7, width=4)
lb.pack(padx=2, pady=2)
e1.pack(padx=2, pady=2)
f_top.pack(padx=2, pady=2)
but.pack(side=LEFT, padx=2, pady=2)
but2.pack(side=LEFT, padx=2, pady=2)
but3.pack(side=LEFT, padx=2, pady=2)
but4.pack(side=LEFT, padx=2, pady=2)
but5.pack(side=LEFT, padx=2, pady=2)
but6.pack(side=LEFT, padx=2, pady=2)
but7.pack(side=LEFT, padx=2, pady=2)
root.mainloop()