import numpy as np
import matplotlib.pyplot as plt
import os

# First run. p = 0.1
os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_2_1.cpp -O3')
os.system('./a.out x.dat 0.01')
data = np.loadtxt('x.dat')
x = data[0]
xsq = data[1]

delxsq = np.diff(xsq)
delxsqLog1 = np.log(delxsq)

# # Second run. p = 0.01
# os.system('g++ CPhys.cpp Vector.cpp Matrix.cpp Cube.cpp part1_2_2.cpp -O3')
# os.system('./a.out')
# data = np.loadtxt('x.dat')
# x = data[0]
# xsq = data[1]

# delxsq = np.diff(xsq)
# delxsqLog2 = np.log(delxsq)

# Calculate once.
N = len(x)
length = np.linspace(0,N-1,N);
lengthLog = np.log10(length[1:])




plt.plot(lengthLog,delxsqLog1)
# plt.plot(lengthLog,delxsqLog2)
# plt.plot(length,xsq)
# plt.plot(length,x)
plt.show()


