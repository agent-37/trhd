import copy

import matplotlib.pyplot as plt
import numpy as np
m =21
n = int(1e3)
a = 0.25
b = 0.75
def pp(l,r):
    if l <a:
        def p(x):
            global a,b
            if x<=a:
                return x/a
            else:
                return (b)/(a-1)*x-(b)/(a-1)
        pl,pr = p(l),p(r)
        mi,ma = min(pl,pr),max(pl,pr)
        return [mi,ma]
    else:
        def p(x):
            global a, b
            if x < a:
                return x / a
            else:
                return (b)/(a-1)*x-(b)/(a-1)

        pl, pr = p(l), p(r)
        mi, ma = min(pl, pr), max(pl, pr)
        return [mi, ma]

inter = []
for i in range(m):
    if (i+1.)/m<a or i/m>a:
        inter.append([i/m,(i+1)/m, 1./m])
    else:
        inter.append([i / m, a, a- i/m])
        inter.append([a, (i + 1) / m, (i + 1) / m - a])
for _ in range(n):
    new_inter= copy.deepcopy(inter)
    for i in range(len(new_inter)):
        new_inter[i][2]=0
    for i in inter:
        otr = pp(i[0],i[1])
        # print(1)
        for j in range(len(new_inter)):
            ll,rr = max(new_inter[j][0],otr[0]), min(new_inter[j][1],otr[1])
            dist = max(0, rr-ll)
            new_inter[j][2] += i[2]*dist / (otr[1]-otr[0])
    inter = copy.deepcopy(new_inter)
ii = []
pos = 0
while pos< len(inter):
    if inter[pos][1]==a:
        ii.append([inter[pos][0],inter[pos+1][1],inter[pos][2]+inter[pos+1][2]])
        pos+=1
    else:
        ii.append(inter[pos])
    pos +=1
res = []
tim = []
for i in ii:
    res.append(i[2]*m)
    tim.append((i[0]+i[1])/2)
plt.plot(tim,res)
plt.show()
