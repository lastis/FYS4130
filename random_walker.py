import numpy as np
import matplotlib.pyplot as plt

blocks = 100000
N = 1000
p = 0.5
dx = 1

x = np.zeros(N)
xsq = np.zeros(N)

for i in xrange(N):
    for block in xrange(blocks):
        ran = np.random.random()
        if (ran > p) :
            x[i] -= 1
        else :
            x[i] += 1
    xsq[i] += x[i]*x[i]
x /= blocks
xsq /= blocks

length = np.linspace(1,N,N);

plt.plot(length,xsq)
plt.show()


