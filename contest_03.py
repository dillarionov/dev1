# -*- coding: utf-8 -*-

# количество скобок, должно быть четное
n = 4
arr = ['(' for _ in range(n // 2)] + [')' for _ in range(n // 2)]


def f(n, arr):
    # печатаем нулевую последовательность
    print (arr)
    while True:
        ind = n - 1
        cnt = 0

        # находим откр. скобку, которую можно заменить
        while ind >= 0:
            if arr[ind] == ')':
                cnt -= 1
            if arr[ind] == '(':
                cnt += 1
            if cnt < 0 and arr[ind] == '(':
                break
            ind -= 1

        # если не нашли, то алгоритм заканчивает работу
        if ind < 0:
            break

        # заменяем на закр. скобку
        arr[ind] = ')'

        # заменяем на самую лексикографическую минимальную
        for i in range(ind + 1, n):
            if i <= (n - ind + cnt) / 2 + ind:
                arr[i] = '('
            else:
                arr[i] = ')'
        print (arr)


f(n, arr)
