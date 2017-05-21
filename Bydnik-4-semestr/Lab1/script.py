from numpy import *
from math import *
phi=lambda x0 : (8/5)*(log(x0)+1)            #сюда функцию в каноническом виде
x0=2                                       #начальное приближение
e=1e-5                                       #точность
n=0
while (True):
    n += 1
    print("Итерация {0} - x сейчас равен {1}".format(n, x0))
    x=phi(x0)
    if abs(x0 - x) <= e:break
    x0=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))
print("Вектор невязки:{0}".format(x0-phi(x0)))