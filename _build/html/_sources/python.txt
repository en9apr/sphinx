======================
Python Quick Reference
======================

Python is a high-level open-source language. This page is written with the **use** of Python in mind, as opposed to computer science definitions. iPython is used here because it means the print statement can be avoided and the output is automatically computed by the iPython interpreter.

Modules
=======

Definition
----------

* Modules provide useful functions, such as array operations, plotting and much more.
* We can import the module to allow access to the functions 

.. ipython::
   
   In [1]: # comments in python are denoted by the hash tag

   In [2]: import numpy as np # for matrix operations

   In [3]: import matplotlib.pyplot as plt # for 2D plotting

* We have defined the following aliases:

  =================== ======= ==================
  Module              Alias   Purpose
  =================== ======= ==================
  numpy               np      Matrix Operations
  matplotlib.pyplot   plt     2D Plotting
  =================== ======= ==================

Use
---

* This allows reference to the modules via the alias, e.g.

.. ipython::
   
   In [1]: myarray = np.linspace(0,5,10)

   In [2]: myarray

* If you don't preface the linspace function with `np` python will throw an error:
* To learn the new functions avaliable to you, visit: `Numpy Reference <http://docs.scipy.org/doc/numpy/reference/>`_
* Or for Matlab users: `Numpy for Matlab Users <http://wiki.scipy.org/NumPy_for_Matlab_Users/>`_

Variables
=========

Definition
----------

Python doesn't require explicitly declared variable types like C and Fortran.

.. ipython::

   In [1]: a = 5 # a is an integer 5

   In [1]: b = 'five' # b is a string of the word 'five'

   In [1]: c = 5.0 # c is a floating point 5

Use
---

Use `type` to determine the type of variable:

.. ipython::

   In [1]: type(a)

   In [2]: type(b)

   In [3]: type(c)

Division using integers is in two ways:

* Integer / Integer = Integer

.. ipython::
   
   In [1]: 14 / 3 

* Integer / Float = Float

.. ipython::

   In [1]: 14 / 3.0 

Whitespace in Python
====================

Python uses indents and whitespaces to group statements together. To write a loop in C you might use:

.. code-block:: c

   for (i = 0, i < 5, i++){
       printf("Hi! \n");
   }

Or in Fortran:

.. code-block:: fortran
   
   do i = 1, 4
       print *, "Hi!" 
       print *, " "
   enddo

Python doesn't use curely braces like C or the enddo like Fortran. The Python equivalent is:

.. code-block:: python

   for i in range(5):
       print "Hi! \n"
