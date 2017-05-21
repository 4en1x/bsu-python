from numpy import *
from math import *
import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function
x = sym.Symbol('x')
s='5*x-8*sym.log(x)-8'                                       #сюда функцию в каноническом виде
f=lambdify(x, eval(s), 'numpy')
f_dash=lambdify(x, sym.diff(eval(s), x, 1), 'numpy')
f_2dash=lambdify(x, sym.diff(eval(s), x, 2), 'numpy')

x0=345345                                                            #начальное приближение
e=1e-5                                                           #точность

n=0
while (True):
    n += 1
    print("Итерация {0} - x сейчас равен {1}".format(n, x0))
    x=x0-f(x0)/f_dash(x0) - (f(x0)**2*f_2dash(x0))/(2* (f_dash(x0)**3));
    if abs(x0 - x) <= e:break
    x0=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))