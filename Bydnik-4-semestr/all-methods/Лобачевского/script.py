a=[1,14,28,0,-160] #сюда массив коэффициентов
p=[0]*len(a)

k=0
while(True):
    k+=1
    print("Итерация {0}".format(k))
    for i in range(0,len(a)):
        p[i]=0
        for s in range(1,i+1):
            if i-s>=0 and i+s<len(a):
                p[i]+=(-1)**s*a[i-s]*a[i+s]
        p[i]*=2
    print("     Массив S: {0}".format(p))
    aNew=[0]*len(a)
    xNew=[0]*len(a)
    for i in range(0,len(a)):
        aNew[i]=a[i]**2+p[i]
    print("     Новые коэффициенты a: {0}".format(aNew))
    for i in range(1, len(a)):
        if aNew[i-1]!=0:
            xNew[i]=(-1)**i*((aNew[i]/aNew[i-1])**(1/(2**k)))
        else : xNew[i]=0
    print("     Вычесленные значения: {0}".format(xNew))
    a=aNew
    if k==10:break