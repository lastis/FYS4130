import numpy as np
import matplotlib.pyplot as plt


# First run. p = 0.5
data = np.loadtxt('x1_5_1.dat')
yData = data[0]
x = data[1]

# a = 0.0005
# y = np.exp(-4)*np.exp(-a*x*x)
# y = np.log(y)
xsq = x*x

# Second run. p = 0.9

# plt.plot(bins,x)
# plt.plot(xsq,y)
plt.plot(xsq,np.log(yData))
plt.show()


