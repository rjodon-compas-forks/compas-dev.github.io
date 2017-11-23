.. _introduction:

********************************************************************************
Introduction
********************************************************************************

.. .. rst-class:: lead

.. ``compas`` is a computational framework for researchers, professionals, and students working in the fields of architecture, engineering, and digital fabrication. It was originally developed at the `Block Research Group <http://block.arch.ethz.ch>`_ of `ETH Zurich <http://www.ethz.ch>`_ for ...

.. Main contributors are 
.. `Tom Van Mele <http://block.arch.ethz.ch/brg/people/tom-van-mele>`_, 
.. `Andrew Liew <http://block.arch.ethz.ch/brg/people/andrew-liew>`_, 
.. `Tomas Mendéz <http://block.arch.ethz.ch/brg/people/tomas-mendez-echenagucia>`_,
.. and `Matthias Rippmann <http://block.arch.ethz.ch/brg/people/matthias-rippmann>`_.


Objectives
----------

* provide a robust computational base for research in architecture, engineering and digital fabrication;
* facilitate collaboration within and among these fields;
* encourage ...; and
* ...


Features
--------

* Open source
* Pure Python core
* Plug-and-play additional functionality
* Wrappers for external libraries
* Interop utilities for easy integration of C/C++
* Integration in CAD software
* ...


Overview
--------

``compas`` is divided into a main library and a pool of user-contributed research packages.
The main library is entirely open source and licensed under the MIT license.
The user-contributed packages are released with access levels defined by the respective
authors. They can be private, public, or shared with a specific group of users.

The reason for this setup is related to the objectives of ``compas``
to facilitate transfer of knowledge generated through research in the fields of
architecture, structures, and fabrication, and encourage and facilitate collaboration.

By building specialised research packages on the main library, these packages are
compatible with each other, allowing expertise and know-how to be shared with, and reviewed
and extended by a large community of researchers and practicioners.

The possibility of defining packages as private, public, or shared, and the possibility
to change this state at any given time, allows researchers to publish their work
in a way that corresponds to the state of their research, to the sensitivities
of collaborations, or to the requirements of their funding.

For example, at the Block Research Group (BRG), we currently work on the packages shown
below, with variable levels of external access. These packages roughly correspond
to the ongoing research projects at BRG.

Main library
------------

The main library consists of a core package (<code>compas</code>) and several additional
packages for integration of the core functionality in CAD software.
The core package defines all <em>real</em> functionality. The CAD packages simply provide
a unified framework for processing, visualising, and interacting with datastructures
and geometrical objects, and building user interfaces in different CAD software.

Here, we only provide an overview of some of the main components.
For the complete documentation of the functionality provided by the main library,
see the API reference (...).


Add-ons
-------
