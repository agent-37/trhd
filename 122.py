import matplotlib.pyplot as plt
import numpy as np
T= 0
h = 0.01

def fk(x, y, z):
    global eps, b, r, s
    return s * (y - x)


def fq(x, y, z):
    global eps, b, r, s
    return x * (r - z) - y


def fd(x, y, z):
    global b, r, s
    return x * y - b * z


def find_dots(x_0_1, x_0_2, x_0_3):
    global T, h
    t_0 = 0

    points_1 = [x_0_1]
    points_2 = [x_0_2]
    points_3 = [x_0_3]
    for i in range(8000):
        k1 = h * fk(x_0_1, x_0_2, x_0_3)
        q1 = h * fq(x_0_1, x_0_2, x_0_3)
        d1 = h * fd(x_0_1, x_0_2, x_0_3)
        k2 = h * fk(x_0_1 + k1 / 2, x_0_2 + q1 / 2, x_0_3 + d1 / 2)
        q2 = h * fq(x_0_1 + k1 / 2, x_0_2 + q1 / 2, x_0_3 + d1 / 2)
        d2 = h * fd(x_0_1 + k1 / 2, x_0_2 + q1 / 2, x_0_3 + d1 / 2)
        k3 = h * fk(x_0_1 + k2 / 2, x_0_2 + q2 / 2, x_0_3 + d2 / 2)
        q3 = h * fq(x_0_1 + k2 / 2, x_0_2 + q2 / 2, x_0_3 + d2 / 2)
        d3 = h * fd(x_0_1 + k2 / 2, x_0_2 + q2 / 2, x_0_3 + d2 / 2)
        k4 = h * fk(x_0_1 + k3, x_0_2 + q3, x_0_3 + d3)
        q4 = h * fq(x_0_1 + k3, x_0_2 + q3, x_0_3 + d3)
        d4 = h * fd(x_0_1 + k3, x_0_2 + q3, x_0_3 + d3)
        x_0_1 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_0_2 += (q1 + 2 * q2 + 2 * q3 + q4) / 6
        x_0_3 += (d1 + 2 * d2 + 2 * d3 + d4) / 6
        # print(x_0_1, x_0_2)
        t_0 += h
        points_1.append(x_0_1)
        points_2.append(x_0_2)
        points_3.append(x_0_3)
        # print(i, h)
    res = []
    res.append(points_1)
    res.append(points_2)
    res.append(points_3)
    T = t_0
    return res

def find_mu(res):
    global T,h
    mu =[0,0,0]
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
    ax = plt.figure().add_subplot(projection='3d')
    for i in range(len(res[0])):
        # ax.plot(res[0], res[1],res[2])
        ax.scatter(res[0][i], res[1][i], res[2][i],c = 'blue')
    ax.legend()
    mu_x = find_mu(res)
    res_c = find_c(res, mu_x)
    plt.figure(2)
    plt.plot(res_c[1], res_c[0])

    plt.show()


eps = 0.1
x_0_1, x_0_2, x_0_3 = map(float, input('Введите начальное значение x_0\n').split())
# a, b = map(float, input('Введите начальное значение параметров').split())
b = 8 / 3
r = 100
s = 10
print_dots(find_dots(x_0_1, x_0_2, x_0_3))
