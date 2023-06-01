#Таценко Алина Дмитриевна 44-22-119 21
from math import sin, cos,sqrt

def func(*args):
    y=[]
    for x in args:
        if x<=0.8:
            y.append( sin(x)**2-sqrt(x**3))
        else:
            y.append( x**2*cos(x)+2*x)
    return y

def main():
    start=input('Введите значения x, разделяя их пробелами: ')
    try:
        nums=[float(x) for x in start.split()]
    except ValueError:
            print('Невозможно преобразовать строку в число')
    except Exception:
            print('Ошибка')
    y=func(*nums)
    print(*y)

if __name__=='__main__':
    main()
