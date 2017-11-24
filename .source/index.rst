.. _index:

********************************************************************************
The compas framework
********************************************************************************

.. figure:: /_images/compas_overview.png
    :figclass: figure
    :class: figure-img img-fluid

    Both the Armadillo Vault and the NEST HiLo roof were developed with ``compas``.

The ``compas`` framework is an open-source, Python-based computational framework
for collaboration and research in architecture, engineering and digital fabrication.
It is developed by the Block Research Group (https://block.arch.ethz.ch) of ETH
Zurich (http://www.ethz.ch), with the support of the NCCR (National Centre
for Competence in Research) on "Digital Fabrication" (http://www.dfab.ch/).
The main contributors are:

* `Tom Van Mele <http://block.arch.ethz.ch/brg/people/tom-van-mele>`_
* `Andrew Liew <http://block.arch.ethz.ch/brg/people/andrew-liew>`_
* `Tomas Mendéz <http://block.arch.ethz.ch/brg/people/tomas-mendez-echenagucia>`_
* `Matthias Rippmann <http://block.arch.ethz.ch/brg/people/matthias-rippmann>`_

The objective of ``compas`` is to provide a robust, flexible, easy-to-learn,
and easy-to-use computational framework for students, researchers, and professionals
working in architecture, engineering, and digital fabrication, and (tangentially)
related fields.

At the Block Research Group (BRG), for several years, ``compas`` has been the
computational base not only for all PhD and postdoc-level research, but also for
all BRG projects, such as the Armadillo Vault, and the NEST HiLo roof.


Multi-disciplinary collaboration
================================

Architecture is a highly multi-disciplinary field, combining research from computer
science, robotics, mathematics, automation, and several other scientific areas.
The target audience of the ``compas`` framework is therefore very diverse.

To deal with the different scientific backgrounds, programming skills, computational
inclinations, and best/accepted practices of its users and their respective fields,
``compas`` is implemented primarily in Python and designed to be entirely independent
of the functionality of CAD software. As a result, it can be used on many different
platforms and in combination with many different types of external software and libraries,
and at the same time take advantage of the many scientific and non-scientific libraries
available in the Python ecosystem itself. Furthermore, and perhaps more importantly, it
ensures that research based on ``compas`` is not tied to a specific CAD-based ecosystem,
as is unfortunately so often the case in architecture and which really gets in the way
of proper scientific collaboration.


Public, Private, Shared
=======================

.. figure:: /_images/compas_overview.png
    :figclass: figure
    :class: figure-img img-fluid

    The framework is divided into a main library and a pool of user-contributed research packages.
    The main library is entirely public (green), while accessibility to the additonal packages
    is entirely controlled by their authors.


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


Main library
============

The main library consists of a core package (``compas``) and several additional
packages for integration of the core functionality in CAD software. The core package
defines all *real* functionality. The CAD packages simply provide a unified framework
for processing, visualising, and interacting with datastructures and geometrical
objects, and building user interfaces in different CAD software.

`The documentation of the main library <http://compas-dev.github.io>`_ provides many more resources for further exploration.


Additional packages
===================



Documentation
=============


Sublime Text Plug-in
====================


