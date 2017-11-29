.. _installation:

********************************************************************************
Installation
********************************************************************************


General steps
=============

**1.** Create a folder on your computer for your COMPAS installation.

.. code-block:: none

    compas-dev


**2.** Clone the repository of the main library from Github

*Using git*

.. code-block:: none
    
    $ cd path/to/compas-dev
    $ git clone https://github.com/compas-dev/compas.git


*Using Github Desktop*

.. code-block:: none

    GitHub Desktop > File > Clone Repository


* Use the *Url* option.
* Repository Url: https://github.com/compas-dev/compas.git
* Local Path: ``path/to/compas-dev/compas``


.. figure:: /_images/github_clonerepo.*
     :figclass: figure
     :class: figure-img img-fluid


After cloning the repository, the folder structure will contain::

    compas-dev
        - compas
            - libs
            - samples
            - src
            - temp


The ``src`` folder should contain several Python packages::

    - compas
    - compas_blender
    - compas_maya
    - compas_rhino


**3.** Configure your system

* Verify that Python is on the system ``PATH``.
* Add the compas framework to the ``PYTHONPATH``.

Operating system-specific instructions can be found below:

* `Unix`_ 
* `Windows`_


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

