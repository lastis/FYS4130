import numpy as np
import matplotlib.pyplot as plt
xFile = open('x.dat','r')
data = np.loadtxt('x.dat')
# x2File = open('x2.dat','r')
# data2 = np.loadtxt('x2.dat')

x = data[0]
xsq = data[1]
N = len(x)
blocks = 1e5

length = np.linspace(1,N,N);
length0 = np.linspace(0,N-1,N);

x0 = x[1:]
lengthLog = np.log10(length0[1:])
# lengthLog = np.log10(length[:-1])
xsqLog = np.log10(xsq[1:])

var = xsq - x*x

delxsq = np.diff(xsq)
delxsqLog = np.log(delxsq)

# x2sq = data2[1]
# x2sqLog = np.log10(x2sq[1:])

plt.plot(length0[:-1],delxsq)
# plt.plot(lengthLog,xsqLog)
# plt.plot(lengthLog[:11],xsqLog[:11])
# plt.plot(lengthLog,lengthLog)
# plt.plot(length0[:11],xsq[:11])
# plt.plot(length0,xsq)
# plt.plot(length0,var)
# plt.plot(length0,x)
plt.show()


