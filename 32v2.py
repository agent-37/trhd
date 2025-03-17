import copy
from random import random

import matplotlib.pyplot as plt
import numpy as np
m =21
n = int(1e3)*2
a = 0.75
b = 0.1
def p(x):
    global a,b
    if x<=a:
        return x/a
    else:
        return b/(a-1)*x-b/(a-1)

inter = []
for i in range(m):
    inter.append([i/m,(i+1)/m, 0])

for _ in range(n):
    cur = random()
    new_inter= copy.deepcopy(inter)
    for _ in range(n):
        cur = p(cur)
        for i in inter:
            if i[0]<cur<i[1]:
                i[2]+=1
res = []
tim = []
h = 1/m
sum = 0
for i in inter:
    sum+= h * i[2]
    print(i)
for i in inter:
    res.append(i[2]/sum)
    tim.append((i[0]+i[1])/2)
plt.plot(tim,res)
plt.show()
