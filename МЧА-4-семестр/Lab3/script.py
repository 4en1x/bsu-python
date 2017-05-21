from numpy import *
from math import *
x0=3.7
e=1e-4
n=0
def phi(x):
    return (8/5)*(log(x) + 1)
while (True):
    n+=1
    x=(x0*phi(phi(x0))-phi(x0)*phi(x0))/(phi(phi(x0))-2*phi(x0)+x0)
    if abs(x0 - x) <= e:break
    x0=x
print("За {0} итераций получили корень {1} с точностью {2}".format(n,x0,e))
print("Вектор невязки:{0}".format(x0-(8/5)*(log(x0)+1)))