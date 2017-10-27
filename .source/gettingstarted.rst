.. _gettingstarted:

********************************************************************************
Getting started
********************************************************************************

Requirements
------------

* Python (`Anaconda <https://www.anaconda.com/download/>`)
* `Rhino3D <https://www.rhino3d.com/download>`
* Code editor (e.g. Sublime Text)
* GitHub Desktop


Installation instructions
-------------------------

**Step 1.** Create a folder structure for your compas installation.

.. code-block:: none

    compas-dev
        - acadia2017
        - compas
        - me


**Step 2.** Clone the code repository from Github, or simply download the archive and unzip in compas/core.

.. code-block:: none

    $ cd path/to/compas/core
    $ git clone https://github.com/compas-dev/compas.git


**Step 3.** Verify your installation.

.. code-block:: none

    $ python

.. code-block:: python

    >>> import compas
    >>> from compas.datastructures import Mesh
    >>> mesh = Mesh.from_obj(compas.get('faces.obj'))
    >>> print(mesh)

.. code-block:: none



.. .. figure:: /_images/example-mesh-delaunay-from-points.*
..     :figclass: figure
..     :class: figure-img img-fluid


Dependencies
------------

The ``compas`` framework has very few dependencies, and most of them are optional. If
you are happy working in Rhino or Blender, and you are not interested in or don't
need any of the numerical stuff, then everything should work out of the box;
provided you have Python installed, of course.

The current version of ``compas`` has the following **optional** dependencies:

* `Numpy <http://www.numpy.org/>`_ &amp; `Scipy <https://www.scipy.org/>`_: For all numerical calculations and algorithms.
* `Matplotlib <http://matplotlib.org/>`_: For two-dimensional visualisations.
* `PyOpenGL <http://pyopengl.sourceforge.net/>`_: For three-dimensional visualisations.
* `PySide <https://wiki.qt.io/PySide>`_: For some of the standalone tools.
* `NetworkX <https://networkx.github.io/>`_: For spring layouts of networks.
* `Planarity <https://github.com/hagberg/planarity>`_: For planarity testing.
* `Cython <http://cython.org/>`_: For performance optimisation.
* `Numba <http://numba.pydata.org/>`_: For just-in-time compilation.
* `PyCuda <https://mathema.tician.de/software/pycuda/>`_: For parallel computation through Nvidia's CUDA.
* `PyOpenCL <https://mathema.tician.de/software/pyopencl/>`_: For parallel computation though OpenCL.
* `CVXPY <http://www.cvxpy.org/>`_: For convex optimisation problems.
* `Imageio <https://imageio.github.io/>`_: For reading and writing of image data.
* `PIL <http://www.pythonware.com/products/pil>`_: For general image processing.

Scientific Python distributions like `Anaconda <https://www.continuum.io/>`_ or
`Enthought EPD <https://www.enthought.com/products/epd/>`_ provide most of the
optional dependencies (and of course Python), or a package manager to
install them with. Make sure to get a version that ships with Python 2.x (see
note above).

On Windows, many installers for remaining and otherwise difficult-to-install packages
can be found on Christof Gholke's page
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
On mac, installing whatever doesn't ship with a scientific distribution is
relatively easy with a package manager like `macports <https://www.macports.org/>`_
or `homebrew <http://brew.sh/>`_.


Environment-specific instructions
---------------------------------

Unix (OSX, Linux)
=================



Windows
=======
