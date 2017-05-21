from numpy import *
from math import *
import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function
x = sym.Symbol('x')
s='5*x-8*sym.log(x)-8'                                       #сюда функцию
f=lambdify(x, eval(s), 'numpy')

x0=3.6                                                            #начальное приближение
x1=3.7                                                             #второе начальное приближение
e=1e-7                                                          #точность
n=0
while (True):
    n += 1
    print("Итерация {0} - x(k-1) сейчас равен {1}, x(k) сейчас равен {2}".format(n, x0,x1))
    x= x1-f(x1)*((x1-x0)/(f(x1)-f(x0)))
    if abs(x1 - x) <= e:break
    x0=x1
    x1=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))