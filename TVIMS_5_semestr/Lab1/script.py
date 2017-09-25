import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

uniform = np.random.uniform(2, 4, 10)

sample_moment_1 = sum(i for i in uniform) / len(uniform)
sample_moment_2 = sum(i * i for i in uniform) / len(uniform)
sample_moment_3 = sum(i * i * i for i in uniform) / len(uniform)

sample_central_moment_1 = sum(i - sample_moment_1 for i in uniform) / len(uniform)
sample_central_moment_2 = sum(i * i - sample_moment_2 for i in uniform) / len(uniform)
sample_central_moment_3 = sum(i * i * i - sample_moment_3 for i in uniform) / len(uniform)

print(uniform)
print('\nВыборочный момент порядка 1: {0:.20f}'.format(sample_moment_1))
print('Выборочный момент порядка 2: {0:.20f}'.format(sample_moment_2))
print('Выборочный момент порядка 3: {0:.20f}'.format(sample_moment_3))

print('\nВыборочный центральный момент порядка 1: {0:.20f}'.format(sample_central_moment_1))
print('Выборочный центральный момент порядка 2: {0:.20f}'.format(sample_central_moment_2))
print('Выборочный центральный момент порядка 3: {0:.20f}'.format(sample_central_moment_3))

t = np.arange(1, 5, 0.0001)

def f(x):
    y = []
    for i in x:
        if i < 2:
            y.append(0)
        elif i > 4:
            y.append(1)
        else:
            y.append((i - 2) / 2)
    return np.array(y)


ecdf = sm.distributions.ECDF(uniform)

x = np.linspace(min(uniform), max(uniform))
y = ecdf(x)
red_patch = mpatches.Patch(color='red', label='Теоретическая функция распределения')
green_patch = mpatches.Patch(color='green', label='Эмпирическая функция распределения')
plt.legend(handles=[red_patch, green_patch])
plt.plot(x, y, color='green', linewidth=1)
plt.plot(t, f(t), color='red', linewidth=1)
plt.show()

def f(x):
    y = []
    for i in x:
        if i < 2 or i > 4:
            y.append(0)
        else:
            y.append(50000)
    return np.array(y)

data = np.random.uniform(2, 4, 1000000)
count, bins, ignored = plt.hist(data, 20, facecolor='green', hatch="/")

orange_patch = mpatches.Patch(color='orange', label='Теоретическая функция распределения')
green_patch = mpatches.Patch(color='green', label='Эмпирическая функция распределения')
plt.legend(handles=[orange_patch, green_patch])

plt.xlabel('X~U[2,4]')
plt.ylabel('Count')
plt.title("Гистограмма равномерного распределения")
plt.axis([1.5, 4.5, 0, 100000])
plt.grid(True)
plt.plot(t, f(t))
plt.show()
