import scipy.optimize as spo
import numpy as np

a = np.asarray([11.5, 92.5, 44.3, 98.1, 20.1, 6.1, 45.5, 31.0, 44.3])


def cost_function(x):
    f = 0
    for i in range(9):
        f = f + (x[i] / a[i])**2
    return f


def cons1(x):
    return 0.0298*x[0] - 0.044*x[1] - 0.044*x[2] - 4


def cons2(x):
    return -0.0138*x[2] + 0.0329*x[3] + 0.0329*x[4] - 0.025*x[5] - 0.025*x[6] - 33


def cons3(x):
    return 0.0279*x[4] - 0.0617*x[6] + 0.0317*x[7] - 0.0368*x[8] - 31


if __name__ == '__main__':
    x0 = np.asarray([5, 5, 5, 5, 5, 5, 5, 5, 5])
    con = ({'type': 'eq', 'fun': cons1},
           {'type': 'eq', 'fun': cons2},
           {'type': 'eq', 'fun': cons3})

    con1 = np.zeros(9)
    res = spo.minimize(cost_function, x0, constraints=con, bounds=((0, None), (0, None), (0, None),
                                                                   (0, None), (0, None), (0, None),
                                                                   (0, None), (0, None), (0, None)))
    print(res)
