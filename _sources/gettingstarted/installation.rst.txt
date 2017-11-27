.. _installation:

********************************************************************************
Installation
********************************************************************************

General steps
=============

**1.** Create a folder on your computer for your compas installation.

.. code-block:: none

    compas-dev


**2.** Clone the code repository from Github using GitHub Desktop

.. code-block:: none

    GitHub Desktop > File > Clone Repository


* Use the *Url* option.
* Repository Url: https://github.com/compas-dev/compas.git
* Local Path: ``path/to/compas-dev/compas``


.. figure:: /_images/github_clonerepo.*
     :figclass: figure
     :class: figure-img img-fluid


After pulling the repository, the folder structure will contain::

    compas-dev
        - compas
            - libs
            - samples
            - src


The ``src`` folder should contain several Python packages::

    - compas
    - compas_blender
    - compas_dynamo
    - compas_grasshopper
    - compas_maya
    - compas_rhino
    - compas_rhinomac


**3.** Configure your system

* Verify that Python has been added to the system ``PATH``.
* Add the compas framework to the ``PYTHONPATH``.

Operating system specific instructions for `Windows`_ and  `Unix`_ can be found below.


**4.** Verify your installation.

After having set the system variables test your installation.
Start an interactive Python session (in Terminal or Command Prompt)::

    $ python


Then try the following code.

.. code-block:: python

    >>> import compas
    >>> compas.verify()


If all required packages are installed, try

.. code-block:: python

    >>> import compas
    >>> from compas.datastructures import Mesh
    >>> mesh = Mesh.from_obj(compas.get('faces.obj'))
    >>> print(mesh)


If on OSX your Terminal window will display as follows

.. figure:: /_images/validate_mac.*
    :figclass: figure
    :class: figure-img img-fluid


In Comand Prompt it will display as follows

.. figure:: /_images/validate_windows_small.*
    :figclass: figure
    :class: figure-img img-fluid


.. _Unix:

On Unix (Linux, OSX)
====================

Open Terminal to edit your system variables. First, find out which ``profile`` file needs to be edited::

    $ cd
    $ ls -a


This will list all files in your home directory.
Check if you have a ``.bash_profile`` or ``.profile``.
Choose the ``.bash_profile``  if it exists, otherwise choose the ``.profile``

To edit your ``.bash_profile``, type::

    $ nano .bash_profile


.. note::
    
    You may be prompted for the administrator password.
    Characters will not appear while you are typing.


Add the following::

    export PATH="/path/to/anaconda/bin:$PATH"
    export PYTHONPATH="/path/to/compas/src:$PYTHONPATH"


.. note::

    You will not be able to copy and paste into the window.
    Make sure to type all paths correctly.


.. figure:: /_images/mac_bashprofile.*
     :figclass: figure
     :class: figure-img img-fluid


After adding the paths, exit the editor with ``ctrl + o``, ``enter``, ``ctrl + x``.
Then restart your Terminal or type::

    $ source .bash_profile


.. _Windows:

On Windows
==========

On Windows, you will have to change your *Environment Variables*::

    Control Panel > System > Advanced system settings > Environment Variables


.. figure:: /_images/windows_controlpanel.*
     :figclass: figure
     :class: figure-img img-fluid


.. figure:: /_images/windows_advancedsystemsettings.*
     :figclass: figure
     :class: figure-img img-fluid


.. figure:: /_images/windows_environment.*
     :figclass: figure
     :class: figure-img img-fluid


In the section *User variables*, edit ``PATH``.

.. note::

    Create a new ``PATH`` variable if one doesn't exist.


.. figure:: /_images/windows_path.*
     :figclass: figure
     :class: figure-img img-fluid


Add the paths to your Anaconda installation.

.. figure:: /_images/windows_path-entries.*
     :figclass: figure
     :class: figure-img img-fluid


Then add ``compas`` to the ``PYTHONPATH``.

.. note::

    Create a new ``PTYTHONPATH`` variable if one doesn't exist.


.. figure:: /_images/windows_pythonpath.*
     :figclass: figure
     :class: figure-img img-fluid


.. figure:: /_images/windows_pythonpath-entries.*
     :figclass: figure
     :class: figure-img img-fluid


Dependencies
============

The ``compas`` framework has very few dependencies, and most of them are optional. If
you are happy working in Rhino or Blender, and you are not interested in or don't
need any of the numerical stuff, then everything should work out of the box;
provided you have Python installed, of course.

The current version of ``compas`` has the following **optional** dependencies:

* `Numpy <http://www.numpy.org/>`_: For all numerical calculations and algorithms.
* `Scipy <https://www.scipy.org/>`_: For all numerical calculations and algorithms.
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
install them with.

On Windows, many installers for remaining and otherwise difficult-to-install packages
can be found on Christof Gholke's page
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
On mac, installing whatever doesn't ship with a scientific distribution is
relatively easy with a package manager like `macports <https://www.macports.org/>`_
or `homebrew <http://brew.sh/>`_.

