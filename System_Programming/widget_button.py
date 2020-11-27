from tkinter import *

root = Tk()
lb = Label(width=15)
e1 = Entry(text='Код цвета', width=15)
e1.insert(0, 'Код цвета')
lb['text'] = 'Цвет'

def vvod1():
    e1.delete(0, END)
    e1.insert(0, "#ff0000")
    lb['text'] = 'Красный'
def vvod2():
    e1.delete(0, END)
    e1.insert(0, "#ff7d00")
    lb['text'] = 'Оранжевый'
def vvod3():
    e1.delete(0, END)
    e1.insert(0, "#ffff00")
    lb['text'] = 'Жёлтый'
def vvod4():
    e1.delete(0, END)
    e1.insert(0, "#00ff00")
    lb['text'] = 'Зелёный'
def vvod5():
    e1.delete(0, END)
    e1.insert(0, "#007dff")
    lb['text'] = 'Голубой'
def vvod6():
    e1.delete(0, END)
    e1.insert(0, "#0000ff")
    lb['text'] = 'Синий'
def vvod7():
    e1.delete(0, END)
    e1.insert(0, "#7d00ff")
    lb['text'] = 'Фиолетовый'

but = Button(bg='#ff0000', command=vvod1, width=15,)
but2 = Button(bg='#ff7d00', command=vvod2, width=15)
but3 = Button(bg='#ffff00', command=vvod3, width=15)
but4 = Button(bg='#00ff00', command=vvod4, width=15)
but5 = Button(bg='#007dff', command=vvod5, width=15)
but6 = Button(bg='#0000ff', command=vvod6, width=15)
but7 = Button(bg='#7d00ff', command=vvod7, width=15)
lb.pack()
e1.pack()
but.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()
root.mainloop()
