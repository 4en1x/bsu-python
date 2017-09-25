import numpy as np
import math
from decimal import Decimal

np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)

A = np.array([[0, 0, 0, 1, 2],  # матрица основных ограничений
              [3, 0, 2, 0, -4],
              [0, -1, 3, 0, 0]])
b = np.array([-4, 25, 6])  # Вектор ресурсов
c = np.array([6, 3, -2, -1, -14])  # Вектор стоимости
d_down = np.array([1, -1, -2, 1, -3])  # Вектор нижних ограничений
d_up = np.array([4, 3, 2, 4, 1])  # Вектор верхних ограниче-ний

x = np.array([11/3, 0, 2, 1, -2.5])  # Начальный вектор ответа

step = 0  # количество шагов

already_check = []
indexes_not_basis = []

while True:

    print('\n\nИтерация номер {0}'.format(step + 1))
    print('Базисный план в начале итерации: {0}'.format(x))

    old_indexes_not_basis = indexes_not_basis
    indexes_not_basis = np.array(list(i for i in range(0, 5) if x[i] == d_down[i] or x[i] == d_up[i]))
    indexes_not_basis = indexes_not_basis[:2]
    indexes_basis = np.setdiff1d(np.array([0, 1, 2, 3, 4]), indexes_not_basis)

    print('Небазисные индексы: {0}; Базисные индексы: {1}'.format(indexes_not_basis + 1, indexes_basis + 1))

    if not np.array_equal(old_indexes_not_basis, indexes_not_basis):
        already_check = []

    A_basis = A[:, indexes_basis]
    C_basis = c[np.array(indexes_basis)]
    print('А базисная:\n {0};'.format(A_basis))
    print('С базисный: {0};'.format(C_basis))

    u = np.linalg.solve(np.transpose(A_basis), C_basis)
    print('Вектор u: {0};'.format(u))

    x_dump = x
    while True:
        delta = np.array(list([c[i] - np.inner(A[:, i], u), i] for i in indexes_not_basis if i not in already_check))
        print('Вектор дельты (вначале вектор значений, затем вектор индексов):\n {0}\n{1};'.format(delta[:, [0]],
                                                                                                   (delta[:, [1]] + 1)))
        main_index = 0
        main_value = Decimal('-Infinity')
        end = 0

        for [d, index] in delta:
            index = math.ceil(index)
            d = math.ceil(d)
            if (math.fabs(x[index] - d_down[index]) < 0.01 and d <= 0) or (
                    math.fabs(x[index] - d_up[index]) < 0.01 and d >= 0):
                end += 1
            if math.fabs(d) > main_value:
                main_index = math.ceil(index)
                main_value = math.fabs(d)
        if end == 2:
            print('Найден оптимальный план')
            break

        print('Оптимальный план не найден, итерируем далее')

        print('j = {0}'.format(main_index))

        l_basis = np.linalg.solve(A_basis, A[:, main_index])
        l = np.zeros(5)
        theta = np.zeros(5)
        counter = 0
        l[main_index] = np.sign(main_value)
        theta[main_index] = d_up[main_index] - d_down[main_index]
        theta_opt = math.fabs(theta[main_index])

        for i in indexes_basis:
            l[i] = -l_basis[counter] * l[main_index]
            if l[i] > 0:
                theta[i] = (d_up[i] - x[i]) / l[i]
            if l[i] < 0:
                theta[i] = (d_down[i] - x[i]) / l[i]
            if l[i] != 0:
                if math.fabs(theta[i]) < theta_opt:
                    theta_opt = math.fabs(theta[i])
            counter += 1

        x = np.array(list(x[i] + theta_opt * l[i] for i in range(0, 5)))

        print('Вектор l: {0};'.format(l))
        print('Вектор theta: {0};'.format(theta))
        print('Оптимальная theta: {0};'.format(theta_opt))
        print('Новый план: {0};'.format(x))

        panic = 0
        for i in range(0, 5):
            if x[i] > d_up[i] or x[i] < d_down[i]:
                panic += 1
        print(x)

        if panic == 0:
            already_check.append(main_index)
            step += 1
            break

        print('План вырожденный, идём находить новую max-ную дельту и новый индекс j, итерация продолжается')
        already_check.append(main_index)
        x = x_dump
    if end == 2: break
print('\n\nНайден оптимальный базисный план, и он равен {0}'.format(x))
