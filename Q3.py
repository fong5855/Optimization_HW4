import scipy.optimize as spo
import numpy as np


def cost_function(x):
    return 5*x[0] + 4*x[1] - x[2]


def cons1(x):
    return x[0] - 2*x[1] - x[2] - 1


def cons2(x):
    return 2*x[0] + x[1] + x[2] - 4


if __name__ == '__main__':
    x0 = np.asarray([5, 5, 5])
    con = ({'type': 'eq', 'fun': cons1},
           {'type': 'eq', 'fun': cons2})

    con1 = np.zeros(9)
    res = spo.minimize(cost_function, x0, constraints=con, bounds=((0, None), (0, None), (None, None)))
    print(res)
