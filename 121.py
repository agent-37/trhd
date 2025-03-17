from cmath import cos, sin, sqrt
from sympy import sin, cos, Matrix, diff, solve, N, symbols
import numpy as np
from sympy.abc import x, y, z, t
import matplotlib.pyplot as plt

T= 0
h = 0.01
def fk(x, y, t):
    global eps, a, b
    return 1 - (b + 1) * x + a * x ** 2 * y


def fq(x, y, t):
    global eps
    return b * x - a * x ** 2 * y


def find_dots(x_0_1, x_0_2):
    global T, h
    t_0 = 0

    points_1 = [x_0_1]
    points_2 = [x_0_2]
    for i in range(200000):
        k1 = h * fk(x_0_1, x_0_2, t_0)
        q1 = h * fq(x_0_1, x_0_2, t_0)
        k2 = h * fk(x_0_1 + k1 / 2, x_0_2 + q1 / 2, t_0 + h / 2)
        q2 = h * fq(x_0_1 + k1 / 2, x_0_2 + q1 / 2, t_0 + h / 2)
        k3 = h * fk(x_0_1 + k2 / 2, x_0_2 + q2 / 2, t_0 + h / 2)
        q3 = h * fq(x_0_1 + k2 / 2, x_0_2 + q2 / 2, t_0 + h / 2)
        k4 = h * fk(x_0_1 + k3, x_0_2 + q3, t_0 + h)
        q4 = h * fq(x_0_1 + k3, x_0_2 + q3, t_0 + h)
        x_0_1 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_0_2 += (q1 + 2 * q2 + 2 * q3 + q4) / 6
        # print(x_0_1, x_0_2)
        t_0 += h
        points_1.append(x_0_1)
        points_2.append(x_0_2)
        # print(i, h)
    res = []
    res.append(points_1)
    res.append(points_2)
    T = t_0
    return res

def find_mu(res):
    global T,h
    mu =[0,0]
    for i in range(len(mu)):
        for j in range(len(res[i])-1):
            mu[i] += h*(res[i][j]+res[i][j+1])/2
        mu[i]/=T
    return mu

def find_c(res, mu):
    res_c = []
    tim = []
    t_0 = 0
    count =0
    global T, h
    while t_0<20:
        cur = 0
        for i in range(len(res[0])-count-1):
            for j in range(len(res)):
                cur+=((res[j][i] - mu[j]) * (res[j][i + count] - mu[j]) +(res[j][i+1] - mu[j]) * (res[j][i + count+1] - mu[j])) * h /2
        cur/=T-t_0
        tim.append(t_0)
        res_c.append(cur)
        t_0+=h
        count+=1
        print(t_0)
    return [res_c,tim]

def print_dots(res):
    plt.figure(1)
    plt.plot(res[0], res[1])
    mu_x = find_mu(res)
    res_c = find_c(res,mu_x)
    plt.figure(2)
    plt.plot( res_c[1],res_c[0])
    plt.show()


eps = 0.1
x_0_1, x_0_2 = map(float, input('Введите начальное значение x_0\n').split())
# a, b = map(float, input('Введите начальное значение параметров').split())
a, b = 1, 3
print_dots(find_dots(x_0_1, x_0_2))
# Найденные параметры для периодического решения
# a,b=1,3
