from math import *
from sympy import *
import numpy as np
import sympy as sp
def binom(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)
def rr(x,y):
	n = len(x)
	v = np.zeros((n,n))
	for j in range(n):
		v[j,0] = y[j]
	for i in range(1,n):
		for j in range(n-i):
			v[j,i] = (v[j+1,i-1]-v[j,i-1])/(x[j+i]-x[j])
	c = v[0,:].copy()
	print("Таблица разделённых разностей:\n")
	print(v)
	return c
def delta(k,y,how):
	if k==0 :return y[how]
	sum=0
	for i in range(k+1):
		sum+=y[k-i+how]*binom(k,i)*pow(-1,i)
	return sum
def rr_ermit(x,y,der,k):
	n = len(x)
	v = np.zeros((n,n))
	for j in range(n):
		v[j,0] = y[j]
	for i in range(1,n):
		for j in range(n-i):
			if((j+i)//k==j//k):
				v[j, i]=(der[i-1][j//k])/factorial(i)
			else:
				v[j,i] = (v[j+1,i-1]-v[j,i-1])/(x[j+i]-x[j])
	c = v[0,:].copy()
	print("Таблица разделённых разностей (часть):\n")
	print(v)
	return c