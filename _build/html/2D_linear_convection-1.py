def convection(nt, nx, ny, tmax, xmax, ymax, c):
   """
   Returns the velocity field and distance for 2D linear convection
   """
   # Increments
   dt = tmax/(nt-1)
   dx = xmax/(nx-1)
   dy = ymax/(ny-1)

   # Initialise data structures
   import numpy as np
   u = np.ones(((nx,ny,nt)))
   x = np.zeros(nx)
   y = np.zeros(ny)

   # Boundary conditions
   u[0,:,:] = u[nx-1,:,:] = u[:,0,:] = u[:,ny-1,:] = 1

   # Initial conditions
   u[(nx-1)/4:(nx-1)/2,(ny-1)/4:(ny-1)/2,0]=2

   # Loop
   for n in range(0,nt-1):
      for i in range(1,nx-1):
         for j in range(1,ny-1):
            u[i,j,n+1] = (u[i,j,n]-c*dt*((1/dx)*(u[i,j,n]-u[i-1,j,n])+
                                         (1/dy)*(u[i,j,n]-u[i,j-1,n])))

   # X Loop
   for i in range(0,nx):
      x[i] = i*dx

   # Y Loop
   for j in range(0,ny):
      y[j] = j*dy

   return u, x, y

def plot_initial_conditions(u,x,y,nt,ny,title):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel('u (m/s)')
   X,Y=np.meshgrid(x,y)
   surf=ax.plot_surface(X,Y,u[:,:,0],rstride=2,cstride=2)
   plt.title(title)
   plt.show()

def plot_middle_conditions(u,x,y,nt,ny,title):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel('u (m/s)')
   X,Y=np.meshgrid(x,y)
   surf=ax.plot_surface(X,Y,u[:,:,((nt-1)/2)],rstride=2,cstride=2)
   plt.title(title)
   plt.show()

def plot_final_conditions(u,x,y,nt,ny,title):
   """
   Plots the 2D velocity field
   """

   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   fig=plt.figure(figsize=(11,7),dpi=100)
   ax=fig.gca(projection='3d')
   ax.set_xlabel('x (m)')
   ax.set_ylabel('y (m)')
   ax.set_zlabel('u (m/s)')
   X,Y=np.meshgrid(x,y)
   surf=ax.plot_surface(X,Y,u[:,:,nt-1],rstride=2,cstride=2)
   plt.title(title)
   plt.show()


u,x,y = convection(101, 81, 81, 0.5, 2.0, 2.0, 0.5)
plot_initial_conditions(u,x,y,51,81,'Figure 1: c=0.5m/s, nt=101, nx=81, ny=81, t=0sec')
plot_middle_conditions(u,x,y,51,81,'Figure 2: c=0.5m/s, nt=101, nx=81, ny=81, t=0.25sec')
plot_final_conditions(u,x,y,51,81,'Figure 3: c=0.5m/s, nt=101, nx=81, ny=81, t=0.5sec')