#!/usr/bin/python3
import numpy as np
from scipy.optimize import linprog



def findEasyAns(arr):
    minmax = [min(arr[0, :]), 0]
    maxmin = [max(arr[:, 0]), 0]
    for i in range(arr.shape[0]):
        m = min(arr[i, :])
        if maxmin[0] < m:
            maxmin = [m, i]
                
    for i in range(arr.shape[1]):
        m = max(arr[:, i])
        if minmax[0] > m:
            minmax = [m, i]
    if minmax[0] == maxmin[0]:
        return np.array([
                [0 if _ != maxmin[1] else 1 for _ in range(arr.shape[0])],
                [0 if _ != minmax[1] else 1 for _ in range(arr.shape[1])]])
    return None
    


def Nash_Equilibrium(arr):
    if not hasattr(arr, "__len__"):
        raise Exception("Argument of Nash_Equilibrium is not an array")
    if len(arr) == 0 or not hasattr(arr[0], "__len__"):
        raise Exception("Argument of Nash_Equilibrium is not a matrix")
    if (len(arr[0]) == 0):
        raise Exception("Argument of Nash_Equilibrium is not a matrix")
    arr = np.array(arr)
    
    # try to find a saddle point
    ans = findEasyAns(arr)
    if ans is not None:
        return ans
    
    # remove negative numbers so the cost of the game is not 0 (strategies do not change)
    off = np.amin(arr)
    off = 0 if off > 0 else -off + 1
    arr += off
        
    # arguments for solution finder
    c = [1] * arr.shape[0]
    a_ub = -arr.T
    b_ub = [-1] * arr.shape[1]
    
    ans1 = linprog(c, A_ub = a_ub, b_ub = b_ub, method = "simplex")
    # normilize answer vector
    p = ans1.x / ans1.fun
    
    # second solution finder
    c = [-1] * arr.shape[1]
    a_ub = arr
    b_ub = [1] * arr.shape[0]
    
    ans2 = linprog(c, A_ub = a_ub, b_ub = b_ub, method = "simplex")
    q = ans2.x / (-ans2.fun)
    
    # return a tuple of both answer vectors and the cost of the game
    return (p, q, (1 / ans1.fun) - off)

