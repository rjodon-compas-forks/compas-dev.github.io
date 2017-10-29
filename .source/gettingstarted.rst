.. _gettingstarted:

********************************************************************************
Getting started
********************************************************************************

Requirements
------------

* Python (`Anaconda <https://www.anaconda.com/download/>`_)
* `IronPython 2.7.5 <http://ironpython.codeplex.com/releases/view/169382>`_
* `Rhino3D <https://www.rhino3d.com/download>`_
* Code editor (e.g. `Sublime Text <https://www.sublimetext.com>`_)
* `GitHub Desktop <https://desktop.github.com>`_


Installation instructions
-------------------------

**Step 1.** Create a folder on your computer for your compas installation.

.. code-block:: none

    compas-dev


**Step 2.** Clone the code repository from Github using GitHub Desktop

* Repository to clone: https://github.com/compas-dev/compas.git

.. code-block:: none

    GitHub Desktop > File > Clone Repository


.. figure:: /_images/clone_repo.*
     :figclass: figure
     :class: figure-img img-fluid


After pulling the repository, the folder structure will contain:

.. code-block:: none

    compas-dev
    - compas
        - libs
        - samples
        - src


The ``src`` folder will contain the packages

.. code-block:: none

    - compas
    - compas_blender
    - compas_dynamo
    - compas_grasshopper
    - compas_maya
    - compas_rhino
    - compas_rhinomac

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

    python

try the following code

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

.. figure:: /_images/validate_windows.*
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

To check type ``cd`` to return to home directory and then ``ls -a`` will list all files in your home directory.

Check if you have a ``.bash_profile`` or ``.profile``.
Choose the ``.bash_profile``  if it exists, otherwise choose the ``.profile``

To edit the ``profile``: type

.. code-block:: none

    sudo nano ~/.bash_profile
    or
    sudo nano ~/.profile

*N.B. you may be prompted for the administrator password, characters will not appear while you are typing.*

The ``profile`` file will be opened.

Add the following:

.. code-block:: none

    export PATH="/path/to/anaconda/bin:$PATH"
    export PYTHONPATH="/path/to/compas/src:$PYTHONPATH"

*N.B. You will not be able to copy and paste into the window. Make sure to type all paths correctly.*

.. figure:: /_images/profile_file.*
     :figclass: figure
     :class: figure-img img-fluid

After adding the paths, exit the editor with ``ctrl+x`` , ``y`` and ``enter``
Now restart your Terminal or type :

.. code-block:: none

    source ~/.bash_profile
    or
    source ~/.profile


Windows
=======

You will need to access the Advanced system settings panel

.. code-block:: none

    Control Panel > System and Security > System > Advanced system settings

Click on the *Environment Variables* button. A window will open.

In the system variables part, click on the ``PATH`` entry and then the *Edit* button

.. figure:: /_images/system_path.*
     :figclass: figure
     :class: figure-img img-fluid

Now add the paths pointing to the Anaconda installation on your computer

.. code-block:: none

    C:\Anaconda2
    C:\Anaconda2\Scripts
    C:\Anaconda2\Library\bin


.. figure:: /_images/add_system.*
     :figclass: figure
     :class: figure-img img-fluid

Click *OK* and follow the same steps to add the ``compas`` path to the ``PYTHONPATH``.

.. code-block:: none

    path\to\compas\src

.. figure:: /_images/python_path_existing.*
     :figclass: figure
     :class: figure-img img-fluid

If there is no ``PYTHONPATH`` entry create it but clicking *New*

.. figure:: /_images/add_python_path.*
     :figclass: figure
     :class: figure-img img-fluid

Rhino 3D configuration
++++++++++++++++++++++++

The path to ``compas`` will need to be added to the *Module Search Paths*

.. code-block:: none

    Tools > PythonScript > Edit

In the Rhino Python Editor:

.. code-block:: none

    Tools > Options

Add the path to ``compas`` and move it to the top of the list

.. code-block:: none

    \path\to\compas\src

.. figure:: /_images/add_compas_path_rhino.*
     :figclass: figure
     :class: figure-img img-fluid

Restart Rhino

Rhino3D uses IronPython to interpret your Python scripts.
It ships with its own version of IronPython. In Rhino 5 this bundled IronPython is a beta version.
You should install your own version of IronPython 2.7.5 and not the newest.

Check your IronPython version in Rhino:

.. code-block:: none

    Tools > PythonScript > Edit

A Rhino Python Editor will open, type :

.. code-block:: python

    import sys
    print sys.version_info

Your Rhino command line should display the version info

.. code-block:: python

    sys.version_info(major=2, minor=7, micro=5, releaselevel='final', serial=0)

.. figure:: /_images/python_version.*
     :figclass: figure
     :class: figure-img img-fluid

If your ``releaselevel`` is not 'final' then use your own IronPython version (2.7.5)

In the Rhino Python Editor:

.. code-block:: none

    Tools > Options

Add the following paths and move them above the existing IronPython paths

.. code-block:: none

    C:\IronPython27
    C:\IronPython27\Lib
    C:\IronPython27\DLLs

Restart Rhino
