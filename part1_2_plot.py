import numpy as np
import matplotlib.pyplot as plt

# First run. p = 0.1
data = np.loadtxt('x1_2_1.dat')
x = data[0]
xsq = data[1]

delxsq = np.diff(xsq)
delxsqLog1 = np.log10(delxsq)

# Second run. p = 0.01
data = np.loadtxt('x1_2_2.dat')
x = data[0]
xsq = data[1]

delxsq = np.diff(xsq)
delxsqLog2 = np.log10(delxsq)

# Second run. p = 0.01
data = np.loadtxt('x1_2_3.dat')
x = data[0]
xsq = data[1]

delxsq = np.diff(xsq)
delxsqLog3 = np.log10(delxsq)

# Calculate once.
N = len(x)
length = np.linspace(0,N-1,N);
lengthLog = np.log10(length[1:])


plt.plot(lengthLog,delxsqLog1,label="p = 0.10")
plt.plot(lengthLog,delxsqLog2,label="p = 0.01")
plt.plot(lengthLog,delxsqLog3,label="p = 0.00")
plt.xlabel("log n")
plt.ylabel("log <delta X^2> ")
plt.legend(loc='upper right')
plt.savefig('part1_2.png')
plt.show()


