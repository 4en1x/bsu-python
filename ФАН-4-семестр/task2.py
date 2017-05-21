from sympy import *
from sympy.core.relational import Relational
x0=0
e=1e-3
n=0
s = Symbol('s')
t = Symbol('t')
while (True):
    n += 1
    print("Итерация {0} - x сейчас равен {1}".format(n, x0))
    l = integrate(s * (t ** 2 - 1) * x0, (t, -1, 1))
    h = lambdify(s, l)
    l=l.subs(s,t)*(1/4)+1+(4/3)*t
    if (Relational(x0 - l, e, '<') == True and n>1): break
    x0=l
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))