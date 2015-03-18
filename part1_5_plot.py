import numpy as np
import matplotlib.pyplot as plt


# First run. p = 0.5
data = np.loadtxt('x1_5_1.dat')
y1 = data[0]
x1 = data[1]
xsq1 = x1*x1
y1Log = np.log(y1)
# Second run. p = 0.9
data = np.loadtxt('x1_5_2.dat')
y2 = data[0]
x2 = data[1]
xsq2 = x2*x2
y2Log = np.log(y2)

# a = 0.0005
# y = np.exp(-4)*np.exp(-a*x*x)
# y = np.log(y)


plt.plot(x1,y1)
plt.plot(x2,y2)
# plt.show()
# plt.plot(xsq1,y1Log)
# plt.plot(xsq2,y2Log)
plt.show()


