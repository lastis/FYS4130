import numpy as np
import matplotlib.pyplot as plt
# First run. p = 0.5
data = np.loadtxt('x1_1_1.dat')
x = data[0]
xsq1 = data[1]

# Second run. p = 0.1
data = np.loadtxt('x1_1_2.dat')
x = data[0]
xsq2 = data[1]


# Third run. p = 0.01
data = np.loadtxt('x1_1_3.dat')
x = data[0]
xsq3 = data[1]

# Calculate once.
N = len(x)
length = np.linspace(0,N-1,N);
lengthLog = np.log10(length[1:])

plt.plot(lengthLog,np.log10(xsq1[1:]),label='p=0.5')
plt.plot(lengthLog,np.log10(xsq2[1:]),label='p=0.1')
plt.plot(lengthLog,np.log10(xsq3[1:]),label='p=0.01')
plt.xlabel("n")
plt.ylabel("<X^2> ")
plt.legend(loc='upper right')
plt.savefig('part1_1.png')
plt.show()


