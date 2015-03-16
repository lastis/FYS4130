import numpy as np
import matplotlib.pyplot as plt
import os


os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_5_1.cpp -O3')
os.system('./a.out')
data = np.loadtxt('x.dat')
yData = data[0]
x = data[1]

# a = 0.0005
# y = np.exp(-4)*np.exp(-a*x*x)
# y = np.log(y)
xsq = x*x


# plt.plot(bins,x)
# plt.plot(xsq,y)
plt.plot(xsq,np.log(yData))
plt.show()


