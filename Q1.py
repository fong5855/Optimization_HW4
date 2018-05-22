import scipy.optimize as spo
import math
import numpy as np


def cost_function(x):
    return -1 * math.pi * (x[0]**2) * x[1]


def cons(x):
    return 2 * math.pi * (x[0]**2) + 2 * math.pi * x[0] * x[1] - 24 * math.pi


if __name__ == '__main__':
    x_list = [5, 5]
    x0 = np.asarray(x_list)
    con = ({'type': 'eq', 'fun': cons})
    res = spo.minimize(cost_function, x0, constraints=con, bounds=spo.Bounds(0, 999))
    print(res)
