.. _cadconfig:

********************************************************************************
CAD configuration
********************************************************************************

Requirements
============

* `IronPython 2.7.5 <http://ironpython.codeplex.com/releases/view/169382>`_
* `Rhino3D <https://www.rhino3d.com/download>`_


Rhino configuration
===================

.. add note about virtual machines
.. add notes about rhinomac
.. configuration options for atom

compas
------

Rhino has its own environment settings.
Therefore, you will have to tell Rhino where to find ``compas`` as well.
To do so, open the Rhino Python Editor::

    Tools > PythonScript > Edit


.. figure:: /_images/rhino_scripteditor.*
     :figclass: figure
     :class: figure-img img-fluid


In the Rhino Python Editor, go::

    Tools > Options


and add the path to ``compas``.

.. figure:: /_images/rhino_paths.*
     :figclass: figure
     :class: figure-img img-fluid


.. note::

    Restart Rhino!


IronPython
----------

Rhino uses IronPython to interpret your Python scripts.
It ships with its own version of IronPython.
In Rhino 5 this bundled IronPython is a beta version.
You should install your own version of IronPython such that everything works properly.

.. note::
    
    Install IronPython 2.7.5, and not the latest version of IronPython.
    Rhino doesn't like it...


To check your IronPython version in Rhino, go to the PythonScript Editor::

    Tools > PythonScript > Edit


There, run the following snippet.

.. code-block:: python

    import sys
    print sys.version_info


This will display something like::

    sys.version_info(major=2, minor=7, micro=5, releaselevel='final', serial=0)


If the ``releaselevel`` is not ``'final'``, install your own version of IronPython 2.7.5
and let Rhino know where it is by adding it to the search paths as before::

    Tools > Options


And add::

    C:\path\to\IronPython275
    C:\path\to\IronPython275\Lib
    C:\path\to\IronPython275\DLLs


.. note::

    Restart Rhino!

