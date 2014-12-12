=====================================
Wave Modelling - the State of the Art
=====================================

Cavaleri et al. "Wave Modelling - the State of the Art", Progress in Oceanography, 75 (2007) pp 603 - 674

.. contents::
   :local:
 
Numerics
========

* Choice of numerical scheme can result in large errors. 
* The central problem for numerics is **cartesian grids**
* **Why do we even use Cartesian grids?** Grids allow conservation terms to be rigorously enforced
* **So what's the problem?** Grids require high spatial and spectral resolution


Error due to low geographic resolution and low spectral resolution
------------------------------------------------------------------

The Problem
~~~~~~~~~~~

Errors are caused by:

* CFL number, which quantifies the number of grid spaces traversed by a packet of energy in one timestep. If ocean scale wind-forcing is present, the resolution depends on the **scale of the metrological features and the wave sensitivity to those features**.
* Relative resolution (i.e. the grid density w.r.t. what we are trying to resolve). Some geographic features may be completely left out in a 0.5 degree to 1 degree resolution global model.

Existing Solutions
~~~~~~~~~~~~~~~~~~

* Just increase the grid density (!) from 1 degree to 0.5 degrees. This increases the computing time and the required temporal resolution (to maintain stability).
* **High spectral resolution is mostly needed for swells** and swell attenuation is really linear.
* **Unstructured grids could provide efficient use of grid density, although may not be less diffusive.**
* High resolution is needed **when we are near the shore**

Future Solutions
~~~~~~~~~~~~~~~~

* **Unstructured grids** are expected to become more prevalent, since scales of variation are shorter near the shoreline. **Offshore wave fields only vary on the scale larger than that of the wind field.**

Error due to numerical scheme for geographic propagation
--------------------------------------------------------

The Problem
~~~~~~~~~~~

Numerical diffusion is the **smearing** of wave energy during propagation due to discretisation. It is not to be confused with **dissipation** which implies energy loss. It is caused by the **even-ordered** truncation error in the finite difference scheme. It is different from **numerical dispersion** which is caused by the **odd-ordered** truncation error. It depends on:

* CFL number
* May also depend on propagation direction


Existing Solutions
~~~~~~~~~~~~~~~~~~

There are two effects here:

1) Minimising numerical diffusion in the 1D case:

* Second order leapfrog scheme, which has zero numerical diffusion (WAM)
* Ultimate Quick-EST scheme and limiter, which is third order in 1D (WW3). Total variance diminishing limiters can be used to control wiggles.

2) The efficacy of the extension to 2D:

* Solve for both dimensions simultaneously
* Propagate each dimension in sequence (this decreases the order of accuracy)
* Implicit schemes in 2D, these are less efficient at oceanic scales (SWAN)
* Semi-Lagrangian schemes

Future Solutions
~~~~~~~~~~~~~~~~

**Semi-Lagrangian schemes** are an attractive alternative to traditional Euler schemes. However, there are two difficulties:

1) Assuring mass conservation is generally less straightforward than with Euler schemes
2) Source/sink terms must be applied along the ray at the Lagrangian stage - doing this computationally efficiently is a challenge.

Error due to the numerical scheme for spectral propagation
----------------------------------------------------------

The Problem
~~~~~~~~~~~

The **"Garden sprinkler effect"**. This where we can't resolve the spectral/frequency content and is due to numerical dispersion caused by truncation error. This is due to the **odd ordered** truncation error. It depends on:

* CFL number
* Relative resolution

Numerical dispersion can result in non-physical "wiggles" in the solution. We can counteract numerical dispersion by:

* Adding diffusion artificially
* Formulating diffusion and dispersion in roughly equal amounts.

Existing Solutions
~~~~~~~~~~~~~~~~~~

* Nobody wants to increase spectral resolution for this - due to computational cost.
* Controllable diffusion can be added
* Grid point averaging can be used
* Or an angular diffusive operator

Future Solutions
~~~~~~~~~~~~~~~~

* Let source/sink terms dictate frequency resolution and increase directional resolution as computing resources allow 
* Numerics and physics needs to become coupled through some parameterisations of physical processes.

Error due to source term integration
------------------------------------

The Problem
~~~~~~~~~~~

1st order Euler method requires time steps of around a few minutes, which is too computationally expensive. Various solutions such as semi-implicit methods with limiters have been tried, but are sensitive to time step size, especially for initial wave growth. 

Existing Solutions
~~~~~~~~~~~~~~~~~~

Three solutions:

1) Dynamically adjustment of timestep using a limiter for the maximum timestep. For large scale applications this is good. However, **for small scale applications (where wind and wave changes occur rapidly over the domain), this is bad because of the small timesteps involved.**

2) Limiter made proportional to step size - but this could prevent convergence. Can also remove limiter proportional to step size. 

3) Spreading numerical method - semi-analytical solution for integration source term, which includes wind-wave input, dissipation term, and exact non-linear energy transfer.

Future Solutions
~~~~~~~~~~~~~~~~

* Alternative non-convergent limiters
* Prototype for convergent limiter with reduced time step dependencies
