from numpy import *
from math import *
import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function

x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')

s1='((x1*(x2+5)-1)/2)**(1/2)'     #сюда функцию в каноническом виде
s2='(x1+3*sym.log(x1,10))**(1/2)'

phi2=lambdify((x1,x2), eval(s2), 'numpy')
phi1=lambdify((x1,x2), eval(s1), 'numpy')


x01=3.5
x02=2.2
e=1e-5                                       #точность
n=0
while (True):
    n += 1
    print("Итерация {0} - x1 сейчас равен {1}, x2 сейчас равен {2}".format(n, x01,x02))
    x1=phi1(x01,x02)
    x2=phi2(x01,x02)
    print("Дельта равна {0} Или {1}".format( abs(x01 - x1), abs(x02 - x2)))
    if abs(x01 - x1) <= e and abs(x02 - x2) <= e :break
    x01=x1
    x02=x2
print("За {0} итераций получили корень {1}, {2} с точностью {3}".format(n,x01,x02,e))