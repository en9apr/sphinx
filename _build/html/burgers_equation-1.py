from math import pi as PI
from math import exp as exp

def convection_diffusion(NT, NX, TMAX, XMAX, NU):
   """
   Returns the velocity field and distance for 1D non-linear convection-diffusion
   """
   # Increments
   DT = TMAX/(NT-1)
   DX = XMAX/(NX-1)

   # Initialise data structures
   import numpy as np
   u = np.zeros((NX,NT))
   u_analytical = np.zeros((NX,NT))
   x = np.zeros(NX)
   t = np.zeros(NT)
   ipos = np.zeros(NX)
   ineg = np.zeros(NX)

   # Periodic boundary conditions
   for i in range(0,NX):
       x[i] = i*DX
       ipos[i] = i+1
       ineg[i] = i-1

   ipos[NX-1] = 0
   ineg[0] = NX-1

   # Initial conditions
   for i in range(0,NX):
       phi = exp( -(x[i]**2)/(4*NU) ) + exp( -(x[i]-2*PI)**2 / (4*NU) )
       dphi = -(0.5/NU)*exp( -(x[i]**2) / (4*NU) ) - (0.5*(x[i]-2*PI) / NU )*exp(-(x[i]-2*PI)**2 / (4*NU) )
       u[i,0] = -2*NU*(dphi/phi) + 4

   # Analytical Solution
   for n in range(0,NT):
       t = n*DT

       for i in range(0,NX):
           phi = exp( -(x[i]-4*t)**2/(4*NU*(t+1)) ) + exp( -(x[i]-4*t-2*PI)**2/(4*NU*(t+1)) )

           dphi = ( -0.5*(x[i]-4*t)/(NU*(t+1))*exp( -(x[i]-4*t)**2/(4*NU*(t+1)) )
               -0.5*(x[i]-4*t-2*PI)/(NU*(t+1))*exp( -(x[i]-4*t-2*PI)**2/(4*NU*(t+1)) ) )

           u_analytical[i,n] = -2*NU*(dphi/phi) + 4

   return u_analytical, x

def plot_diffusion(u,x,nt,title):
   """
   Plots the 1D velocity field
   """

   import matplotlib.pyplot as plt
   import matplotlib.cm as cm
   plt.figure()
   colour=iter(cm.rainbow(np.linspace(0,20,nt)))
   for i in range(0,nt,20):
      c=next(colour)
      plt.plot(x,u[:,i],c=c)
   plt.xlabel('x (radians)')
   plt.ylabel('u (m/s)')
   plt.ylim([0,8.0])
   plt.xlim([0,2.0*PI])
   plt.title(title)
   plt.show()

u,x = convection_diffusion(151, 151, 0.5, 2.0*PI, 0.1)
plot_diffusion(u,x,151,'Figure 1: nu=0.1, nt=151, nx=151, tmax=0.5s')