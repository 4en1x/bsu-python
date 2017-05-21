from numpy import *
from math import *
import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function
x = sym.Symbol('x')
s='(8/5)*(sym.log(x) + 1)'                                       #сюда функцию в каноническом виде
f=lambdify(x, eval(s), 'numpy')

x0=12345345                                                             #начальное приближение
e=1e-7                                                          #точность
n=0
while (True):
    n += 1
    print("Итерация {0} - x сейчас равен {1}".format(n, x0))
    x=(x0*f(f(x0))-f(x0)*f(x0))/(f(f(x0))-2*f(x0)+x0)
    if abs(x0 - x) <= e:break
    x0=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))