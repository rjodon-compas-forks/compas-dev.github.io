.. _introduction:

********************************************************************************
Introduction
********************************************************************************

``compas`` is a computational framework for collaboration and research in
architecture, engineering and digital fabrication.
The framework is developed by the Block Research Group (https://block.arch.ethz.ch)
of ETH Zurich (http://www.ethz.ch), with the support of the NCCR (National Centre
for Competence in Research) on "Digital Fabrication" (http://www.dfab.ch/).
Currently, the main contributors are:

* `Tom Van Mele <http://block.arch.ethz.ch/brg/people/tom-van-mele>`_
* `Andrew Liew <http://block.arch.ethz.ch/brg/people/andrew-liew>`_
* `Tomas Mendéz <http://block.arch.ethz.ch/brg/people/tomas-mendez-echenagucia>`_
* `Matthias Rippmann <http://block.arch.ethz.ch/brg/people/matthias-rippmann>`_

The objective of the framework is to provide a robust, flexible, easy-to-learn,
and easy-to-use computational base for students, researchers, and professionals
working in architecture, engineering, and digital fabrication,
and (tangentially) related fields.

At the Block Research Group (BRG), for several years, ``compas`` has been the
computational base not only for all PhD and postdoc-level research, but also for
all BRG projects, such as the Armadillo Vault, and the NEST HiLo roof.


Features
========

More and more, architecture is (again) becoming a highly multi-disciplinary field,
combining research from engineering, computer science, robotics, mathematics, ...
To accomodate the different habits, programming styles, scientific backgrounds,
skill levels, and working environments preferences (operating systems, tool chains, ...)
of a wide variety of users from these differnet fields, ``compas`` has been designed
according to the fllowing principles: 

* Open source
* Pure Python core
* Plug-and-play additional functionality
* Wrappers for external libraries
* Interop utilities for easy integration of C/C++
* Integration in CAD software

.. steep learning curve (as in easy-to-learn)
.. different programming styles
.. different scientific backgrounds
.. high-level and low-level entry points
.. independent of CAD software
.. platform independent
.. standalone plotters and viewers
.. integration with CAD software
.. interfaces to exteranl software (FEA, DEM, NUM, ...)
.. interoperability with C/C++
.. wrappers for external (HPC) libraries
.. plug-and-play functionality
.. supports different environments, platforms, 


Structure
=========

``compas`` is divided into a main library and a pool of user-contributed research
packages. The main library is entirely open source and subject to the MIT license.
The user-contributed packages are released with access levels defined by the respective
authors. They can be private, public, or shared with a specific group of users.

The reason for this setup is related to the objectives of ``compas`` to facilitate
transfer of knowledge generated through research in the fields of architecture,
engineering, (digital) fabrication, and related fields, and encourage and facilitate
collaboration.

By building specialised research packages on the main library, these packages are
compatible with each other, allowing expertise and know-how to be shared with,
and reviewed and extended by a large community of researchers and practicioners.

The possibility of defining packages as private, public, or shared, and the possibility
to change this state at any given time, allows researchers to publish their work
in a way that corresponds to the state of their research, to the sensitivities
of collaborations, or to the requirements of their funding.


.. figure:: /_images/compas_overview.png
    :figclass: figure
    :class: figure-img img-fluid

    ``compas`` is divided into a main library and a pool of user-contributed research packages.


Main library
============

The main library consists of a core package (``compas``) and several additional
packages for integration of the core functionality in CAD software. The core package
defines all *real* functionality. The CAD packages simply provide a unified framework
for processing, visualising, and interacting with datastructures and geometrical
objects, and building user interfaces in different CAD software.

`The documentation of the main library <http://compas-dev.github.io>`_ provides many more resources for further exploration.


Add-ons
=======

Currently, 
