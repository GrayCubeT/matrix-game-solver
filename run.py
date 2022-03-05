#!/usr/bin/python3

from solution.task1 import Nash_Equilibrium
import numpy as np

n = int(input("введите количество строк в матрице игры: "))
if n == 0:
    exit()
arr = [list(map(int, input().split())) for _ in range(n)]
m = len(arr[0])
for i in arr:
    if len(i) != m:
        raise Exception("Количество столбцов в матрице не совпадает.")
arr = np.array(arr)
ans = Nash_Equilibrium(arr)
print("ответ:\n1й игрок: ", ans[0])
print("2й игрок: ", ans[1])
print("значение игры: ", ans[2])
