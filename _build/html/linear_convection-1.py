# Constants
nt = 151
tmax = 0.5
dt =  tmax/(nt-1)
nx =  51
xmax = 2.0
dx = xmax/(nx-1)
c = 1

# Initialise data structures
import numpy as np
u = np.zeros((nx,nt))
x = np.zeros(nx)

# Boundary conditions
u[0,:] = u[nx-1,:] = 1

# Initial conditions
for i in range(1,nx-1):
    if(i > (nx-1)/4 and i < (nx-1)/2):
        u[i,0] = 2
    else:
        u[i,0] = 1

# Loop
for n in range(0,nt-1):
    for i in range(1,nx-1):
        u[i,n+1] = u[i,n]-c*(dt/dx)*(u[i,n]-u[i-1,n])

# X Loop
for i in range(0,nx):
    x[i] = i*dx

import matplotlib.pyplot as plt
plt.figure()
for i in range(0,nt,10):
    plt.plot(x,u[:,i],'r')
plt.xlabel('x (m)')
plt.ylabel('u (m/s)')
plt.ylim([0,2.2])
plt.title('c=1m/s')
plt.show()


# Loop
for n in range(0,nt-1):
    for i in range(1,nx-1):
        u[i,n+1] = u[i,n]-0.5*(dt/dx)*(u[i,n]-u[i-1,n])

import matplotlib.pyplot as plt
plt.figure()
for i in range(0,nt,10):
    plt.plot(x,u[:,i],'r')
plt.xlabel('x (m)')
plt.ylabel('u (m/s)')
plt.title('c=0.5m/s')
plt.ylim([0,2.2])
plt.show()