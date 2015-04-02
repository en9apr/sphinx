.. The Visual Room documentation master file, created by
   sphinx-quickstart on Sat Nov 29 08:59:24 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================
Notes on Computation
====================

The notes that follow are based on the following MOOCs:

* "12 Steps to Navier-Stokes" by `Professor Lorena Barba <http://www.seas.gwu.edu/lorena-barba>`_
* "High Performance Scientific Computing" by `Professor Randall LeVeque <http://depts.washington.edu/amath/staff-members/randy-leveque/>`_ 
* "An Introduction to Interactive Programming in Python" by `Professor Joe Warren <http://report.rice.edu/sir/faculty.detail?p=A2D78585F9777919>`_ et al.
* "Algorithmic Thinking" by `Professor Luay Nakhleh <http://www.cs.rice.edu/~nakhleh/>`_ et al. 

==========
CFD Theory
==========
 
Introduction to CFD and the Navier-Stokes Equations:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   cfd
   continuity
   momentum
   navier_stokes

The Finite Difference Method:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   finite_difference_method
   order_of_accuracy
   explicit_implicit
   finite_difference_formulas_in_2D

Analysis of Numerical Schemes:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   numerical_scheme_1
   numerical_schemes_2
   analysis_of_numerical_schemes
   von_neumann_stability_analysis

Finite Difference Solution of the Navier-Stokes Equations:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   poisson_for_pressure
   marker_and_cell_method
   ghost_cells

Numerical Methods for Linear Hyperbolic Equations:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   courant_number
   new_convection_schemes
   heavy_side_and_sinusoidal_input
   second_order_formulas
   spectral_analysis
 
Numerical Methods for Non-linear Hyperbolic Equations:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   multi_step_methods
   conservative_form
   explicit_implicit_non_linear_convection
   strong_weak

Linear Solvers:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   tri_diagonal_matrix

Finite Difference Solution of the Euler Equations:

.. toctree::
   :maxdepth: 1
   :numbered: 4

   euler_equations_in_vector_form
   discrete_euler
   the_riemann_problem
   sods_test_problem

============
CFD Projects
============

.. toctree::
   :maxdepth: 1
   :numbered: 4

   linear_convection   
   non_linear_convection
   diffusion
   burgers_equation
   2D_linear_convection
   2D_non_linear_convection
   2D_linear_diffusion
   2D_burgers_equation

===========================================
CFD Projects in iPython Notebooks on GitHub
===========================================
   
* `2D Laplace Equation <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Laplace.ipynb>`_
* `2D Poisson Equation <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Poisson.ipynb>`_
* `2D Navier Stokes Equations: Cavity Flow (Loop Method) <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Navier_Stokes_Cavity_Loops.ipynb>`_
* `2D Navier Stokes Equations: Cavity Flow (NumPy Method) <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Navier_Stokes_Cavity_Slices.ipynb>`_
* `2D Navier Stokes Equations: Channel Flow <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Navier_Stokes_Channel.ipynb>`_
* `Leapfrog, Lax-Friedrichs and Lax-Wendroff Schemes: Linear Convection & Heaviside Function <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/New_Convection_Schemes.ipynb>`_
* `Leapfrog, Lax-Friedrichs and Lax-Wendroff Schemes: Linear Convection & Sinusoidal Function <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Linear_Convection_Sinusoidal_Input.ipynb>`_
* `Lax-Friedrichs, Lax-Wendroff and MacCormack Schemes: Non-linear Convection <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Lax_Friedrichs_Lax_Wendroff_and_MacCormack_Schemes.ipynb>`_
* `1D Fourier's Equation with Jacobi and Crank-Nicholson <http://nbviewer.ipython.org/github/en9apr/sphinx/blob/master/Crank_Nicholson.ipynb>`_

==========
Literature
==========

.. toctree::
   :maxdepth: 1
   :numbered: 4

   harlow_and_welch
   thompson
   noakes
   drikakis
   fawehinmi
   cavaleri
   ravel
   feng
   wen
   wen_mobbs

=====================================
High Performance Scientific Computing
=====================================

.. toctree::
   :maxdepth: 1
   :numbered: 4
   
   hpsc

======
Python
======

.. toctree::
   :maxdepth: 1
   :numbered: 4

   python
   comments_strings_print_statements
   arithmetic_expressions
   logical_expressions
   relational_expressions
   assignment_sentences
   conditional_sentences
   variables_and_constants
   functions
   modules
   practice   

================
Programming Tips
================

.. toctree::
   :maxdepth: 1
   :numbered: 4

   programming_tips_1

=============
Helpful Links
=============

* `MathJax Syntax <http://en.wikipedia.org/wiki/Help:Displaying_a_formula>`_
* :ref:`search`

