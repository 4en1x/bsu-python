from numpy import *
phi=lambda x0 : (1-4*x0**2)/12
x0=0
e=1e-4
n=0
while (True):
    n += 1
    print("Итерация {0} - x сейчас равен {1}".format(n, x0))
    x=phi(x0)
    if abs(x0 - x) <= e:break
    x0=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))
print("Вектор невязки:{0}".format(x0-phi(x0)))



