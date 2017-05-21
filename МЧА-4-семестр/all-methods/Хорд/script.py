from numpy import *
from math import *
import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function
x = sym.Symbol('x')
s='5*x-8*sym.log(x)-8'                                       #сюда функцию
f=lambdify(x, eval(s), 'numpy')

x0=3.6                                                            #начальное приближение
x_forewer_x=3.7                                                    #тут не x0 , как в конспекте, а один из концов отрезка
e=1e-7                                                          #точность
n=0
while (True):
    n += 1
    print("Итерация {0} - x сейчас равен {1}".format(n, x0))
    x= x0-f(x0)*((x0-x_forewer_x)/(f(x0)-f(x_forewer_x)))
    if abs(x0 - x) <= e:break
    x0=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))