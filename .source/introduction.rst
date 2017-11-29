.. _introduction:

********************************************************************************
The COMPAS framework
********************************************************************************

.. figure:: /_images/compas_intro.jpg
    :figclass: figure
    :class: figure-img img-fluid


COMPAS is an open-source, Python-based computational framework
for collaboration and research in architecture, engineering and digital fabrication.
It is developed by the Block Research Group (https://block.arch.ethz.ch) of ETH
Zurich (http://www.ethz.ch), with the support of the NCCR (National Centre
for Competence in Research) on "Digital Fabrication" (http://www.dfab.ch).
The main contributors are:
`Tom Van Mele <http://block.arch.ethz.ch/brg/people/tom-van-mele>`_, 
`Andrew Liew <http://block.arch.ethz.ch/brg/people/andrew-liew>`_, 
`Tomas Méndez Echenagucia <http://block.arch.ethz.ch/brg/people/tomas-mendez-echenagucia>`_ and
`Matthias Rippmann <http://block.arch.ethz.ch/brg/people/matthias-rippmann>`_.


Features
========

* a pure Python base with flexible datastructures, algorithms, and methods geared towards applications in architecture, engineering, and fabrication;
* geometry processing independent of CAD tools;
* interoperability with C/C++ code and libraries such as ShapeOp, libigl and Eigen;
* methods and solvers for numerical computation built around NumPy and SciPy;
* high peformance computing through GPU acceleration and JIT compilation;
* plotters and viewers for two-dimensional and basic three-dimensional visualization; and
* interfaces to common CAD software and ecosystems.


.. Objectives
.. ==========

.. importance of documentation
.. learning resource
.. development environment
.. transparency
.. 


Multi-disciplinary research
===========================

Architecture is a highly multi-disciplinary field, combining research from computer
science, robotics, mathematics, automation, and several other scientific areas.
The target audience of the COMPAS framework is therefore very diverse.

To deal with the different academic backgrounds, programming skills, computational
experience, and best/accepted practices of its users and their respective fields,
COMPAS is implemented primarily in Python and designed to be entirely independent
of the functionality of CAD software. As a result, it can be used on different
platforms and in combination with external software and libraries, and at the same
time take advantage of the various scientific and non-scientific libraries available
in the Python ecosystem itself. Furthermore, and perhaps more importantly, it ensures
that research based on COMPAS is not tied to a specific CAD-based ecosystem,
as this can hinder effective collaboration between different users.


Public, Private, Shared
=======================

.. .. figure:: /_images/compas_overview.png
..     :figclass: figure
..     :class: figure-img img-fluid
.. 
..     The framework is divided into a main library and a pool of user-contributed research packages.
..     The main library is entirely public, while accessibility to the additonal packages
..     is entirely controlled by their authors.


COMPAS is divided into a main library and a pool of user-contributed research
packages. The main library is entirely open source and subject to the MIT license.
The user-contributed packages are released with access levels defined by the respective
authors. They can be private, public, or shared with a specific group of users.

The reason for this setup is related to the objectives of COMPAS to facilitate
the transfer of knowledge generated through research in the fields of architecture,
engineering, digital fabrication, and related fields, and to facilitate
collaboration.

By building specialised research packages on the main library, these packages are
compatible with each other, allowing expertise and know-how to be shared with,
and reviewed and extended by a large community of researchers and practicioners.

The possibility of defining packages as private, public, or shared, and the possibility
to change this state at any given time, allows researchers to publish their work
in a way that corresponds to the state of their research, to the sensitivities
of collaborations, or to the requirements of their funding.


Main library
============

The main library consists of a core package (`compas`) and several additional
packages for integration of the core functionality in CAD software (`compas_rhino`, `compas_blender`, `compas_maya`).
The core package defines all *real* functionality. The CAD packages simply provide
a unified framework for processing, visualising, and interacting with datastructures
and geometrical objects, and for building user interfaces in different CAD software.

`The documentation of the main library <https://compas-dev.github.io>`_ provides
many more resources for further exploration. `The API reference <https://compas-dev.github.io/main/reference.html>`_
contains detailed information about the functionality of the core package and the CAD packages.


Additional packages
===================

The additional packages supplement the main library with functionality related to
specialised topics. These packages can be related to ongoing or completed research,
or simply provide additional functionality, as a service to other users. For an overview
of available packages, see https://compas-dev.github.io/packages/.


Resources
=========

* `COMPAS home <http://compas-dev.github.io>`_
* `COMPAS main library <http://compas-dev.github.io/main/>`_
* `COMPAS additional packages <http://compas-dev.github.io/packages/>`_
* `COMPAS forum <http://forum.compas-framework.org>`_
* `COMPAS development group <http://github.com/compas-dev>`_
* `COMPAS main library repo <http://github.com/compas-dev/compas>`_

