#Таценко Алина Дмитриевна 44-22-119 21
from math import sin, cos,sqrt
from tkinter import*
from tkinter.messagebox import showerror
def func():
    XEnter = enter.get()
    try:
        x=float(XEnter)
        if x<=0.8:
            y= sin(x)**2-sqrt(x**3)
        else:
            y=  x**2*cos(x)+2*x
        labelAnsw['text']= y
    
    except ValueError:
             showerror(title="Ошибка", message='Невозможно преобразовать строку в число')
             enter.delete(0, END)


root = Tk()
root.title('Task 3')
root.geometry('900x300')
labelX = Label(font = 'Times 24')
labelX['text'] = 'Введите  значение аргумента:'
labelX.pack()
enter = Entry(width = 20,font = 'Times 24')
enter.pack()
buttonEnter = Button(text = 'Рассчитать', font = 'Times 24',command=func)
buttonEnter.pack()
labelY = Label(font = 'Times 24')
labelY['text'] = 'Значение функции равно : '
labelY.pack()
labelAnsw = Label(font = 'Times 24')
labelAnsw['text'] = ''
labelAnsw.pack()
root.mainloop()

