import numpy as np
import matplotlib.pyplot as plt
import os


os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_5_1.cpp -O3')
os.system('./a.out')
data = np.loadtxt('x.dat')
x = data[0]
bins = data[1]

# bins = np.linspace(-100,100,len(x))

plt.plot(bins,x)
plt.show()


