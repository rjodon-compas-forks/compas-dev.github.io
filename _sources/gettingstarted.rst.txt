.. _gettingstarted:

********************************************************************************
Getting started
********************************************************************************

Requirements
------------

* Python (`Anaconda <https://www.anaconda.com/download/>`_)
* `Rhino3D <https://www.rhino3d.com/download>`_
* Code editor (e.g. `Sublime Text <https://www.sublimetext.com>`_)
* `GitHub Desktop <https://desktop.github.com>`_


Installation instructions
-------------------------

**Step 1.** Create a folder on your computer for your compas installation.

.. code-block:: none

    compas-dev


**Step 2.** Clone the code repository from Github using GitHub Desktop

* GitHub Desktop > File > Clone Repository

* Repository to clone: https://github.com/compas-dev/compas.git

.. figure:: /_images/git_hub_clone.jpg
     :figclass: figure
     :class: figure-img img-fluid

After pulling the repository, the folder structure will contain:
.. code-block:: none

    compas
      -libs
      -samples
      -src

The ``src`` folder will contain the packages

* compas
* compas_blender
* compas_dynamo
* compas_grasshopper
* compas_maya
* compas_rhino
* compas_rhinomac

**Step 3.** Configure your system

To simplify importing modules in different contexts a few environment variables need to be set.
Add the Python and/or Scientific Python distribution (in this case the installed version of Anaconda)
to the system ``PATH`` and add the location of the pulled framework to your ``PYTHONPATH``

Operating system specific instructions for Windows and Unix (OSX) can be found at the bottom of this page under
**Environment-specific instructions**

**Step 4.** Verify your installation.

After having set the system variables test your installation.
Start an interactive Python session (in Terminal/ Comand Prompt)
.. code-block:: none

    $ python

try the following code
.. code-block:: python

    >>> import compas
    >>> from compas.datastructures import Mesh
    >>> mesh = Mesh.from_obj(compas.get('faces.obj'))
    >>> print(mesh)

If on OSX your Terminal window will display as follows

.. figure:: /_images/validate_install_mac.jpg
    :figclass: figure
    :class: figure-img img-fluid


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

Unix (OSX)
=================

Open Terminal to edit your system variables. First, find out which ``profile`` file needs to be edited.
To check run:

.. code-block:: none

    cd (will return to home directory)
    ls -a (will list all files in home directory)

You will get a window similar to the one seen below.
Check if you have a ``.bash_profile`` or ``.profile``.
If a ``.bash_profile`` exists this file needs to be edited, otherwise  the  ``.profile`` file

.. figure:: /_images/home_files.*
     :figclass: figure
     :class: figure-img img-fluid

To edit type ``sudo nano ~/.bash_profile`` or ``sudo nano ~/.profile``
*you may be prompted for the administrator password. This will not appear while you are typing.*

The ``profile`` file will be opened. You can now add the following

.. code-block:: none

    export PATH="/path/to/anaconda/bin:$PATH"
    export PYTHONPATH="/path/to/compas/src:$PYTHONPATH"

You will not be able to copy and paste into the window. Make sure to type all paths correctly.

.. figure:: /_images/profile_file.*
     :figclass: figure
     :class: figure-img img-fluid

After adding the paths, exit the editor with `` ctrl+x`` , ``y`` and `` enter``
Now restart your Terminal or type :

.. code-block:: none

    source ~/.bash_profile
    or
    source ~/.profile


Windows
=======
