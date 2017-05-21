from numpy import *
import numpy as np
from math import *
import sympy as sym
from sympy.utilities.lambdify import lambdify, implemented_function

x1 = sym.Symbol('x1')
x2 = sym.Symbol('x2')

s1='x1+x2-3'     #сюда функцию в каноническом виде
s2='x1**2+x2**2-9'

phi2=lambdify((x1,x2), eval(s2), 'numpy')
phi1=lambdify((x1,x2), eval(s1), 'numpy')

phi1_dash_x1=lambdify((x1,x2), sym.diff(eval(s1), x1, 1), 'numpy')
phi1_dash_x2=lambdify((x1,x2), sym.diff(eval(s1), x2, 1), 'numpy')
phi2_dash_x1=lambdify((x1,x2), sym.diff(eval(s2), x1, 1), 'numpy')
phi2_dash_x2=lambdify((x1,x2), sym.diff(eval(s2), x2, 1), 'numpy')

x01=1
x02=5


e=1e-5                                       #точность
n=0
while (True):
    n += 1
    print("Итерация {0} - x1 сейчас равен {1}, x2 сейчас равен {2}".format(n, x01, x02))
    arr = np.array([[phi1_dash_x1(x01,x02),phi1_dash_x2(x01, x02)],[phi2_dash_x1(x01, x02),phi2_dash_x2(x01, x02)]],np.float32)
    arr2 = np.array([[phi1(x01,x02)],[phi2(x01,x02)]],np.float32)

    print("W сейчас такое:\n{0}".format(arr))
    print("\nW^(-1) сейчас такое:\n{0}".format(linalg.inv(arr)))
    arr2=arr2*(-1)

    print("\nF сейчас такое:\n{0}".format(arr2))
    s=linalg.inv(arr).dot(arr2)
    print("\nдельта(от x) сейчас такое:\n{0}".format(s))
    x1=x01+(s)[0][0]
    x2=x02+(s)[1][0]
    x01=x1
    x02=x2




    y=np.array([[phi1(x01,x02)],[phi2(x01,x02)]],np.float32)-arr2*(-1)
    print("\n y сейчас такой:\n{0}".format(y))
    Wnew=arr+((y-arr.dot(s))*s.transpose())/(s.transpose().dot(s))
    print("\n Wnew сейчас такое:\n{0}".format(Wnew))
    snew=linalg.inv(Wnew).dot(np.array([[phi1(x01,x02)],[phi2(x01,x02)]],np.float32)*(-1))
    print("\n второе дельта сейчас такое:\n{0}".format(snew))
    x1=x01+(snew)[0][0]
    x2=x02+(snew)[1][0]


    print("Дельта равна {0} Или {1}".format( abs(x01 - x1), abs(x02 - x2)))
    if abs(x01 - x1) <= e and abs(x02 - x2) <= e :break
    x01=x1
    x02=x2
print("За {0} итераций получили корень {1}, {2} с точностью {3}".format(n,x01,x02,e))