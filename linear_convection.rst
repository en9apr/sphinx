====================
1D Linear Convection
====================

.. contents::
   :local:

Understand the Problem
======================

* What is the final velocity profile for 1D linear convection when the initial conditions are a square wave and the boundary conditions are constant?

* 1D linear convection is described as follows:

.. math:: {\partial u \over \partial t} + c {\partial u \over \partial x} = 0

Formulate the Problem
=====================

Input Data
~~~~~~~~~~

* `nt` = 51 (number of temporal points)
* `nx` = 21 (number of spatial points)
* `tmax` = 0.5
* `xmax` = 2
* `c` = 1

====================== ========================== ========================= ======================== ===========
x                      n                           t                        i                        u(x,t)
====================== ========================== ========================= ======================== ===========
:math:`0`              :math:`0`                  :math:`0 \le t \le 0.5`   :math:`0 \le i \le 20`   :math:`1`
:math:`0 < x \le 0.5`  :math:`0 < n \le 12.5`     :math:`0`                 :math:`0`                :math:`1`
:math:`0.5 < x \le 1`  :math:`12.5 < n \le 25`    :math:`0`                 :math:`0`                :math:`2`
:math:`1 < x < 2`      :math:`25 < n < 50`        :math:`0`                 :math:`0`                :math:`1`
:math:`2`              :math:`50`                 :math:`0 \le t \le 0.5`   :math:`0 \le i \le 20`   :math:`1`
====================== ========================== ========================= ======================== ===========


Output Data
~~~~~~~~~~~

====================== ========================= =========================
x                      t                         u(x,t)
====================== ========================= =========================
:math:`0 < x < 2`      :math:`0.5`               :math:`?`
====================== ========================= =========================


Design Algorithm to Solve Problem
=================================

Space-time discretisation
~~~~~~~~~~~~~~~~~~~~~~~~~

* i :math:`\rightarrow` index of grid in x
* n :math:`\rightarrow` index of grid in t

Numerical scheme
~~~~~~~~~~~~~~~~

* FD in time
* BD in space

Discrete equation
~~~~~~~~~~~~~~~~~

.. math::

   {{u_i^{n+1} - u_i^n} \over {\Delta t}} + c {{u_i^n - u_{i-1}^n} \over \Delta x}=0 

Transpose
~~~~~~~~~

.. math::

   u_i^{n+1} = u_i^n - c{\Delta t \over \Delta x}(u_i^n - u_{i-1}^n)
   
Pseudo-code
~~~~~~~~~~~

::

   #Constants
   nt = 51
   tmax = 0.5
   dt =  tmax/(nt-1) 
   nx =  21
   xmax = 2
   dx = xmax/(nx-1)

   #Boundary Conditions
   for i between 0 and 20
      u(0,i)=1
      u(50,i)=1 
   
   #Initial Conditions
   for n between 1 and 49
      if(12.5 < n < 25)
          u(n,0) = 2
      else
          u(n,0) = 1
   
   #Iteration
   for i between 1 and 20
      u(n+1,i) = u(n,i)-c*(dt/dx)*(u(n,i)-u(n,i-1)
   


Implement Algorithm in Python
=============================

Run the Algorithm on the Data
=============================


