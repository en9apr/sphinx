def non_linear_convection(nt, nx, tmax, xmax):
   """
   Returns the velocity field and distance for 1D non-linear convection
   """
   # Increments
   dt = tmax/(nt-1)
   dx = xmax/(nx-1)

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
         u[i,n+1] = u[i,n]-u[i,n]*(dt/dx)*(u[i,n]-u[i-1,n])

   # X Loop
   for i in range(0,nx):
      x[i] = i*dx

   return u, x

def plot_convection(u,x,nt,title,every):
   """
   Plots the 1D velocity field
   """

   import matplotlib.pyplot as plt
   import matplotlib.cm as cm
   plt.figure()
   colour=iter(cm.rainbow(np.linspace(0,15,nt)))

   for i in range(0,nt,every):
      c=next(colour)
      plt.plot(x,u[:,i],c=c)
      plt.xlabel('x (m)')
      plt.ylabel('u (m/s)')
      plt.ylim([0,2.2])
      plt.title(title)
      plt.show()

u,x = non_linear_convection(151, 151, 0.5, 2.0)
plot_convection(u,x,151,'Figure 1: tmax=0.5s, nt=151, nx=151', 10)

u,x = non_linear_convection(151, 151, 1.0, 2.0)
plot_convection(u,x,151,'Figure 2: tmax=1s, nt=151, nx=151', 10)