import matplotlib.pyplot as plt
import numpy as np



def fk(x, y, z):
    global eps, b, r, s
    return x *y -z


def fq(x, y, z):
    global eps, b, r, s
    return x-y


def fd(x, y, z):
    global b, r, s
    return x + 0.3*z


def find_dots(x_0_1, x_0_2, x_0_3):
    t_0 = 0
    h = 0.1
    points_1 = [x_0_1]
    points_2 = [x_0_2]
    points_3 = [x_0_3]
    for i in range(200):
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
        if max(abs(x_0_1),abs(x_0_2),abs(x_0_3)) >5:
            break
        # print(i, h)
    res = []
    res.append(points_1)
    res.append(points_2)
    res.append(points_3)
    return res


def print_dots(res):
    global ax
    for i in range(len(res[0])):
        ax.plot(res[0], res[1],res[2], c = 'blue')
        # ax.scatter(res[0][i], res[1][i], res[2][i], c='blue')



ax = plt.figure().add_subplot(projection='3d')
# ax.quiver(0 ,0,0,1,1,1, arrow_length_ratio=0.1, color='r')
eps = 0.1
for x_0_1 in range(-1,1+1):
    for x_0_2 in range(-1, 1+1):
        for x_0_3 in range(-1, 1+1):
            # print(x_0_1,x_0_2,x_0_3)
            print_dots(find_dots(x_0_1/1, x_0_2/1, x_0_3/1))

plt.show()
