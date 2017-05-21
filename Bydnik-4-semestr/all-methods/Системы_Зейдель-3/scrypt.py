from numpy import *
from math import *
import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function

x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')
x3 = sym.Symbol('x3')

s1='((x1*(x2+5)-1)/2)**(1/2)'     #сюда функцию в каноническом виде
s2='(x1+3*sym.log(x1,10))**(1/2)'
s3='(x1+x2)'

phi3=lambdify((x1,x2,x3), eval(s3), 'numpy')
phi2=lambdify((x1,x2,x3), eval(s2), 'numpy')
phi1=lambdify((x1,x2,x3), eval(s1), 'numpy')


x01=3.5
x02=2.2
x03=2.2


e=1e-5                                       #точность
n=0
while (True):
    n += 1
    print("Итерация {0} - x1 сейчас равен {1}, x2 сейчас равен {2},x3 сейчас равен {3}".format(n, x01,x02,x03))
    x1=phi1(x01,x02,x03)
    x2=phi2(x1,x02,x03)
    x3 = phi3(x1, x2, x03)
    print("Дельта равна {0} Или {1} Или {2}".format( abs(x01 - x1), abs(x02 - x2), abs(x03 - x3)))
    if abs(x01 - x1) <= e and abs(x02 - x2) <= e and abs(x03 - x3) <= e:break
    x01=x1
    x02=x2
    x03 = x3
print("За {0} итераций получили корень {1},{2} ,{3} с точностью {4}".format(n,x01,x02,x03,e))