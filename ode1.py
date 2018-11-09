"""
Created on Thu Nov  8 21:58:13 2018

@author: james

ODE example

dx/dt = x - y + (xy/1000)
dy/dt = 4x - 2y

"""

from scipy.integrate import odeint
from numpy import arange

# time scale
t = arange(0,15,0.1)

# ODE
def der(state, t):
    x,y = state
    xy1 = x - y + x*y/1000
    xy2 = 4*x - 2*y
    return [xy1, xy2]

# solve ODE
solution_x_y = odeint(der, [2,3], t)

# unpack x & y
x = solution_x_y[:,0]
y = solution_x_y[:,1]

# draw and run plot
import matplotlib.pyplot as plt

plt.close('all')

fig = plt.figure(2)
plt.plot(t, x, '--', t,y)
plt.title('Graph 1: x and versus time')
plt.xlabel('time, s')
plt.ylabel('x and y')
plt.legend(('x','y'))

fig = plt.figure(1)
plt.plot(x[0], y[0], 'o', x,y, 'r')

plt.title('Graph 2: Phase Diagram')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('start', 'run'))
