import numpy as np
import math
from decimal import Decimal

np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)


n = 5  #размеры
m = 3

A = np.array([[0, 4, 0, -5, 0],  # матрица основных ограничений
              [2, 0, 1, 0, 0],
              [0, 4, 0, -1, 2]])

b = np.array([-12, 12, 4])  # Вектор ресурсов
c = np.array([8, 10, 2, -7, 4])  # Вектор стоимости
d_down = np.array([2, 2, -1, 0, -2])  # Вектор нижних ограничений
d_up = np.array([6, 7, 4, 5, 3])  # Вектор верхних ограниче-ний

x = np.array([6, 13/4, 0, 5, -2])  # Начальный вектор ответа
indexes_basis = np.array([2, 3, 5])
step = 0  # количество шагов

indexes_basis -= 1

while True:
    print('\n\nИтерация номер {0}'.format(step + 1))
    print('Базисный план в начале итерации: {0}'.format(x))

    indexes_not_basis = np.setdiff1d(np.array(list(range(n))), indexes_basis)

    print('Небазисные индексы: {0}; Базисные индексы: {1}'.format(indexes_not_basis + 1, indexes_basis + 1))

    A_basis = A[:, indexes_basis]
    C_basis = c[np.array(indexes_basis)]
    print('А базисная:\n {0};'.format(A_basis))
    print('С базисный: {0};'.format(C_basis))

    u = np.linalg.solve(np.transpose(A_basis), C_basis)
    print('Вектор u: {0};'.format(u))

    delta = np.array(list([c[i] - np.inner(A[:, i], u), i] for i in indexes_not_basis ))

    delta_not_complete = []
    delta_map = {}

    for [d, index] in delta:
        index = int(index)
        delta_map[index] = d
        if (math.fabs(x[index] - d_down[index]) < 0.01 and d >= 0) or (math.fabs(x[index] - d_up[index]) < 0.01 and d <= 0):
            delta_not_complete.append(index)

    print('Вектор дельты (индекс: значение):\n {0}'.format(delta_map))
    print('Индексы дельты, для которых не выполняется КО: {0}'.format(delta_not_complete))

    if not delta_not_complete:
        break

    main_index = max(delta_not_complete, key = lambda j: math.fabs(delta_map[j]))

    print('j = {0}'.format(main_index + 1))

    l_basis = np.linalg.solve(A_basis, -1 * np.sign(delta_map[main_index]) * A[:, main_index])
    print('Вектор l базисная: {0};'.format(l_basis))

    l = np.zeros(n)
    l[main_index] = np.sign(delta_map[main_index])
    count = 0
    for i in indexes_basis:
        l[i] = l_basis[count]
        count += 1
    print('Вектор l: {0};'.format(l))

    theta = np.array([float('inf')]*n)
    theta[main_index] = d_up[main_index] - d_down[main_index]
    for i in indexes_basis:
        if l[i] > 0:
            theta[i] = (d_up[i] - x[i]) / l[i]
        if l[i] < 0:
            theta[i] = (d_down[i] - x[i]) / l[i]

    print('Вектор theta: {0};'.format(theta))

    j_star = np.argmin(theta)
    theta_opt = np.min(theta)
    print('j звёздочка: {0};'.format(j_star))
    print('Оптимальная theta: {0};'.format(theta_opt))

    x = np.array(list(x[i] + theta_opt * l[i] for i in range(n)))
    print('Новый план: {0};'.format(x))

    if main_index != j_star:
        indexes_basis = np.array(list( i for i in indexes_basis if i!=j_star))
        indexes_basis = np.append(indexes_basis, main_index)

    step += 1
print('\n\nНайден оптимальный базисный план, и он равен {0}'.format(x))
