import numpy as np
import matplotlib.pyplot as plt
from pylab import exp
from scipy import optimize



# Paramter fitting init
norfunc = lambda p, x : p[0]*exp(-p[1]*x**2) # The full normal function.
fitfunc = lambda p, x : np.log(p[0]) - p[1]*x # Target function.
errfunc = lambda p, x, y : fitfunc(p, x) - y # Distance to the target function.
p0 = [0.02, 0.0005] # Inital try. 



# First run. p = 0.5
data = np.loadtxt('x1_5_1.dat')
# Remove the first and last value for estetics. 
y1 = data[0]
x1 = data[1]
xsq1 = x1*x1
y1Log = np.log(y1)
# Remove some middle points.
mid = len(y1)/2 + 1
remArr = []
nRemove = 0 # Must be odd.
for i in xrange(nRemove):
    index = i - nRemove/2 
    remArr.append(mid + index)
y1Red = np.delete(y1,remArr)
x1Red = np.delete(x1,remArr)
xsq1Red = x1Red*x1Red
y1LogRed = np.log(y1Red)
p1, success = optimize.leastsq(errfunc,p0[:], args=(xsq1Red,y1LogRed))
y1Fit = norfunc(p1,x1)
y1LogFit = fitfunc(p1,xsq1)

# Second run. p = 0.9
data = np.loadtxt('x1_5_2.dat')
y2 = data[0][60:-60]
x2 = data[1][60:-60]
xsq2 = x2*x2
y2Log = np.log(y2)
# Remove some middle points.
mid = len(y2)/2 + 1
remArr = []
nRemove = 0 # Must be odd.
for i in xrange(nRemove):
    index = i - nRemove/2 
    remArr.append(mid + index)
y2Red = np.delete(y2,remArr)
x2Red = np.delete(x2,remArr)
xsq2Red = x2Red*x2Red
y2LogRed = np.log(y2Red)
p2, success = optimize.leastsq(errfunc,p0[:], args=(xsq2Red,y2LogRed))
y2Fit = norfunc(p2,x2)
y2LogFit = fitfunc(p2,xsq2)


plt.plot(x1,y1Fit)
plt.plot(x1,y1,"rx")
plt.plot(x2,y2Fit)
plt.plot(x2,y2,"bx")
plt.show()
# plt.plot(xsq1,y1LogFit)
# plt.plot(xsq1,y1Log,"rx")
# plt.show()
# plt.plot(xsq2,y2LogFit)
# plt.plot(xsq2,y2Log,"bx")
# plt.show()


