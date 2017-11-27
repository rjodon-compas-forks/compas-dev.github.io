.. _userguide:

********************************************************************************
User Guide
********************************************************************************

*Under construction...*


.. where to find what
.. writing a simple script
.. entry points / use cases
.. naming conventions
.. report issues/bugs
.. setting up sublime
.. setting up a project
.. known issues


A simple script
===============

.. code-block:: python



Dependencies
============

**compas** has very few dependencies, and most of them are optional.

====================== ======================== ================================
package                dependencies             exceptions
====================== ======================== ================================
compas.com             None                     :class:`MatlabEngine` (matlab), :class:`MatlabSession` (matlab), ssh.py (paramiko)
compas.datastructures  None
compas.files           None
compas.geometry        None                     xxx_numpy (NumPy, SciPy)
compas.hpc             Numba, PyCuda, PyOpenCL
compas.interop         None
compas.numerical       NumPy, SciPy
compas.plotters        Matplotlib
compas.topology        None                     xxx_numpy (NumPy, SciPy), :func:`network_is_planar` (planarity), :func:`network_embed_in_plane` (NetworkX)
compas.utilities       None                     animation.py (imageio)
compas.viewers         PyOpenGL, PySide
====================== ======================== ================================

Most dependencies are bundled with scientific Python distributions such as
Anaconda or EPD. Refer to the `Getting started instructions <https://compas-dev.github.io/gettingstarted.html>`_
if you need help getting these installed.


Importing stuff
===============

All packages are structured such that functionality can be imported from the *second* level.


Use cases
=========

The functionality of *compas* is implemented independent of the functionality provided
by CAD software. This 


Naming conventions
==================


Reporting issues
================


Setting up a project
====================


Setting up Sublime Text
=======================


Resources
=========

* `compas framework: portal site <http://compas-dev.github.io>`_
* `compas framework: main library docs <http://compas-dev.github.io/main/>`_
* `compas framework: overview additional packages <http://compas-dev.github.io/packages/>`_
* `compas framework: discussion forum <http://forum.compas-framework.org>`_
* `compas framework: main library github repo <http://github.com/compas-dev/compas>`_
